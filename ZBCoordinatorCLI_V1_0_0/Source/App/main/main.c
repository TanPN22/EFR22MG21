 /* File name: main.c
 *
 * Description:
 *
 *
 * Last Changed By:  $Author: TanPN$
 * Revision:         $Revision: $
 * Last Changed:     $Date: $
 *
 *
 ******************************************************************************/
/******************************************************************************/
/*                              INCLUDE FILES                                 */
/******************************************************************************/
#include "af.h"
#include "main.h"
#include "Source/Mid/button/button.h"
#include "Source/Mid/Led/Led.h"
#include "Source/App/Network/network.h"
#include "em_chip.h"
/******************************************************************************/
/*                     PRIVATE TYPES and DEFINITIONS                         */
/******************************************************************************/


/******************************************************************************/
/*                     EXPORTED TYPES and DEFINITIONS                         */
/******************************************************************************/


/******************************************************************************/
/*                              PRIVATE DATA                                  */
/******************************************************************************/

/******************************************************************************/
/*                              EXPORTED DATA                                 */
/******************************************************************************/
uint8_t ledlevel = 0;
/******************************************************************************/
/*                            PRIVATE FUNCTIONS                               */
/******************************************************************************/
void buttonCallbackHandler(uint8_t button, BtnState state);
static bool clusterONHandler(EmberAfClusterCommand* cmd);
static bool clusterCTLHandler(EmberAfClusterCommand* cmd);

EmberEventControl DimledControl;
/******************************************************************************/
/*                            EXPORTED FUNCTIONS                              */
/******************************************************************************/

/******************************************************************************/
/** @brief Main Init
 *
 * This function is called from the application's main function. It gives the
 * application a chance to do any initialization required at system startup.
 * Any code that you would normally put into the top of the application's
 * main() routine should be put into this function.
        Note: No callback
 * in the Application Framework is associated with resource cleanup. If you
 * are implementing your application on a Unix host where resource cleanup is
 * a consideration, we expect that you will use the standard Posix system
 * calls, including the use of atexit() and handlers for signals such as
 * SIGTERM, SIGINT, SIGCHLD, SIGPIPE and so on. If you use the signal()
 * function to register your signal handler, please mind the returned value
 * which may be an Application Framework function. If the return value is
 * non-null, please make sure that you call the returned function from your
 * handler to avoid negating the resource cleanup of the Application Framework
 * itself.
 *
 */
void emberAfMainInitCallback(void)
{
	emberAfCorePrintln("emberAfMainInitCallback");
	buttonInit(buttonCallbackHandler);
	TIM_Init();
//	NetworkInit();
//	emberEventControlSetDelayMS(DimledControl, 100);
}

void buttonCallbackHandler(uint8_t button, BtnState state){
	if(button == BUTTON0)
	{
		switch (state){
		case release:
			emberAfCorePrintln("SW1 is Released");
			dimLed(LED_1, ledRed, 50);
			break;
		case press_1:
			emberAfCorePrintln("SW1 is Pressed");
//			NetworkInit();
			break;
		default:
			break;
		}
	} else if(button == BUTTON1){
		switch (state){
		case release:
			emberAfCorePrintln("SW2 is Released");
			break;
		case press_1:
			emberAfCorePrintln("SW2 is Pressed");
			break;
		default:
		break;
		}
	}
}


bool emberAfPreCommandReceivedCallback(EmberAfClusterCommand* cmd)
{
	if (cmd -> clusterSpecific)
	{
		switch (cmd -> apsFrame -> clusterId)
		{
		case ZCL_ON_OFF_CLUSTER_ID:
			clusterONHandler(cmd);
			break;

		case ZCL_LEVEL_CONTROL_CLUSTER_ID:
			clusterCTLHandler(cmd);
			break;

		default:
			break;
		}
	}
  return false;
}

static bool clusterONHandler(EmberAfClusterCommand* cmd)
{
	return false;
}

static bool clusterCTLHandler(EmberAfClusterCommand* cmd)
{
	uint8_t commandID = cmd->commandId;
	uint8_t endPoint = cmd -> apsFrame ->destinationEndpoint;
	uint16_t payloadOffset = cmd ->payloadStartIndex;
	uint8_t level;

	switch (commandID) {
		case ZCL_MOVE_TO_LEVEL_COMMAND_ID:
			if (cmd -> bufLen < payloadOffset + 1u) {return EMBER_ZCL_STATUS_MALFORMED_COMMAND;}
			level = emberAfGetInt8u(cmd->buffer, payloadOffset, cmd->bufLen);

            emberAfCorePrintln("RECEIVE_HandleLevelControlCluster LEVEL= %d\n",level);
            if (endPoint == 1){
            if(level>=70)
            {
                onLed(LED_1 | LED_2 ,ledGreen);
            }else if(level>=40)
            {
            	onLed(LED_1 | LED_2,ledRed);
            }else if(level>0)
            {
            	onLed(LED_1 | LED_2,ledBlue);
            }else
            {
                offLed(LED_1 | LED_2);
            }
            }else if (endPoint == 2){
            	dimLed(LED_2, ledRed, level);
            }
			break;
		default:
			break;
	}
}

void DimledHandler(void)
{
	emberEventControlSetInactive(DimledControl);
//	dimLed(LED_2, ledRed, ledlevel);
//	emberAfCorePrintln("Led Level: %d", ledlevel);
//	ledlevel ++;
//	if (ledlevel == 100)ledlevel = 0;
	emberEventControlSetDelayMS(DimledControl,100);
}

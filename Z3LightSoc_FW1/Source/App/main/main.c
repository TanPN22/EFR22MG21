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
#include EMBER_AF_API_NETWORK_STEERING
#include "zigbee-framework/zigbee-device-common.h"
#include "Source/Mid/button/button.h"
#include "Source/Mid/LED/led.h"
#include "Source/App/Send/send.h"
#include "Source/App/Network/network.h"
#include "Source/App/Received/received.h"
#include "protocol/zigbee/stack/include/binding-table.h"
#include "app/framework/plugin/network-steering/network-steering.h"
#include "app/framework/plugin/network-steering/network-steering-internal.h"
#include "em_chip.h"
#include "main.h"
/******************************************************************************/
/*                     PRIVATE TYPES and DEFINITIONS                         */
/******************************************************************************/
EmberEventControl mainStateEventControl;
/******************************************************************************/
/*                     EXPORTED TYPES and DEFINITIONS                         */
/******************************************************************************/


/******************************************************************************/
/*                              PRIVATE DATA                                  */
/******************************************************************************/

/******************************************************************************/
/*                              EXPORTED DATA                                 */
/******************************************************************************/
static SystemState_t systemState = POWER_ON_STATE;

uint8_t ledlevel = 0;
static uint8_t       networkReady=false;
/******************************************************************************/
/*                            PRIVATE FUNCTIONS                               */
/******************************************************************************/
void USER_buttonPressAndHoldEventHandle(uint8_t button, uint8_t pressTime);
void USER_buttonHoldingEventHandle(uint8_t button, uint8_t holdTime);
void USER_networkEventHandle(uint8_t networkResult);

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
	emberAfCorePrintln("Main Init");
	ledInit();
	buttonInit(USER_buttonHoldingEventHandle,USER_buttonPressAndHoldEventHandle);

	NETWORK_Init(USER_networkEventHandle);

	emberEventControlSetActive(mainStateEventControl);
}

void mainStateEventHandle(void)
{
	emberEventControlSetInactive(mainStateEventControl);
	EmberNetworkStatus nwkStatusCurrent;

	switch (systemState) {
		case POWER_ON_STATE:
			nwkStatusCurrent = emberAfNetworkState();
			if (nwkStatusCurrent == EMBER_NO_NETWORK)
			{
				toggleLed(LED1, ledRed, 3, 300, 300);
			}else
			{
				toggleLed(LED1, ledPink, 3, 300, 300);
			}

			systemState = IDLE_STATE;

			break;

		case IDLE_STATE:
			break;

		case REBOOT_STATE:
			systemState=IDLE_STATE;
			SendZigDevRequest();
			halReboot();
			break;

		case REPORT_STATE:
			toggleLed(LED1,ledPink,3,300,300);
			networkReady=true;
//			emberAfCorePrintln("Send report to HC bellow");
			SEND_ReportInfoToHc();
			systemState=IDLE_STATE;

			break;

		default:
			break;
	}

	emberEventControlSetInactive(mainStateEventControl);


}

void USER_buttonHoldingEventHandle(uint8_t button, uint8_t holdingEvent)
{
	emberAfCorePrintln("SW %d HOLDING %d s\n",button+1,holdingEvent-press_max);

	switch (holdingEvent)
	{
	case hold_1s:

		break;
	case hold_2s:

		break;
	case hold_3s:

		break;
	case hold_4s:
		toggleLed(LED_ALL, ledGreen, 2, 100, 100);
		break;
	default:
		break;
	}
}


void USER_buttonPressAndHoldEventHandle(uint8_t button, uint8_t pressAndHoldEvent)
{
	if((pressAndHoldEvent >press_max) && (pressAndHoldEvent < hold_max))
	{
		emberAfCorePrintln("SW %d HOLD %d s\n",button+1,pressAndHoldEvent-press_max);
	}else if((pressAndHoldEvent >0) && (pressAndHoldEvent < press_max))
	{
		emberAfCorePrintln("SW %d PRESS_TIME %d\n",button+1,pressAndHoldEvent);
	}else
	{
		emberAfCorePrintln("UNKNOWN\n");
	}

	switch (pressAndHoldEvent)
	{

	case press_1:
		if(button==SW_1)
		{
			turnOnLed(LED1,ledBlue);
			SEND_OnOffStateReport(1,LED_ON);
			SEND_BindingInitToTarget(SOURCE_ENDPOINT_PRIMARY,
									 DESTINATION_ENDPOINT,
									 true,
									 HC_NETWORK_ADDRESS);
//			SEND_OnOffToGroup(1,0,LED_ON,HC_NETWORK_ADDRESS);
		}else
		{
			turnOnLed(LED2,ledBlue);
			SEND_OnOffStateReport(2,LED_ON);
//			SEND_OnOffToGroup(1,0,LED_ON,HC_NETWORK_ADDRESS);
		}
		break;
	case press_2:
		if(button==SW_1)
		{
			emberAfCorePrintln("OFF LED 1");
			turnOffRBGLed(LED1);
			SEND_OnOffStateReport(1,LED_OFF);
			SEND_BindingInitToTarget(SOURCE_ENDPOINT_PRIMARY,
									 DESTINATION_ENDPOINT,
									 false,
									 HC_NETWORK_ADDRESS);
//			SEND_OnOffToGroup(1,0,LED_OFF,HC_NETWORK_ADDRESS);
		}else
		{
			emberAfCorePrintln("OFF LED 2");
			turnOffRBGLed(LED2);
			SEND_OnOffStateReport(2,LED_OFF);
//			SEND_OnOffToGroup(1,0,LED_OFF,HC_NETWORK_ADDRESS);
		}
		break;
	case press_3:
		if(button==SW_1)
		{
			emberAfPluginFindAndBindTargetStart(1);
			toggleLed(LED1,ledyellow,3,200,200);
		}else
		{
			emberClearBindingTable();
			halReboot();
			toggleLed(LED2,ledcyan,3,200,200);
		}

		break;
	case press_4:
		if(button==SW_1)
		{
			toggleLed(LED2,ledRGB,3,200,200);
		}else
		{
			emberClearBindingTable();
			halReboot();
			toggleLed(LED2,ledcyan,4,200,200);
		}
		break;
	case (press_4+1):

		break;
	case hold_1s:
		break;
	case hold_2s:
		break;

	case hold_3s:

		break;
	case hold_4s:
		if(button==SW_1)
		{
			NETWORK_FindAndJoin();
		}else
		{
			NETWORK_Leave();
		}
		break;
	case unknown:
		break;
	default:
		break;
	}

}

void USER_networkEventHandle(uint8_t networkResult)
{
	emberAfCorePrintln("USER_networkEventHandle");
	switch (networkResult)
	{
	case NETWORK_HAS_PARENT:
		systemState=REPORT_STATE;
		emberEventControlSetInactive(mainStateEventControl);
		emberEventControlSetDelayMS(mainStateEventControl,1000);
		break;
	case NETWORK_JOIN_FAIL:
		systemState=IDLE_STATE;
		emberEventControlSetInactive(mainStateEventControl);
		emberEventControlSetActive(mainStateEventControl);
		break;
	case NETWORK_JOIN_SUCCESS:
		systemState=REPORT_STATE;
		emberEventControlSetInactive(mainStateEventControl);
		emberEventControlSetActive(mainStateEventControl);
		break;
	case NETWORK_LOST_PARENT:
		systemState=IDLE_STATE;

		emberEventControlSetInactive(mainStateEventControl);
		emberEventControlSetActive(mainStateEventControl);
		break;
	case NETWORK_OUT_NETWORK:
		if(networkReady)
		{
			emberAfCorePrintln("NETWORK_OUT_NETWORK");
			toggleLed(LED1,ledPink,3,300,300);
			systemState=REBOOT_STATE;
			emberEventControlSetInactive(mainStateEventControl);
			emberEventControlSetDelayMS(mainStateEventControl,3000);
		}
		break;
	default:
		break;
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
//			clusterCTLHandler(cmd);
			break;

		default:
			break;
		}
	}
  return false;
}

static bool clusterONHandler(EmberAfClusterCommand* cmd)
{
		uint8_t commandID = cmd -> commandId;
	    uint8_t endPoint  = cmd -> apsFrame -> destinationEndpoint;
	    uint8_t msgtype	  = cmd -> type;

	    emberAfCorePrintln("RECEIVE_HandleOnOffCluster SourceEndpoint= %d, CommandID = %d\n",endPoint,commandID);

	    switch (msgtype) {
			case EMBER_INCOMING_UNICAST:
				emberAfCorePrintln("Unicast receive");
				break;

			case EMBER_INCOMING_MULTICAST:
				emberAfCorePrintln("Multicast receive");
				break;
			default:
				break;
		}

	    switch(cmd -> commandId)
	    {
		case ZCL_OFF_COMMAND_ID:
			if(endPoint==1)
			{
				emberAfCorePrintln("OFF LED 1");
				turnOffRBGLed(LED1);
				SEND_OnOffStateReport(1,LED_OFF);
			}else if (endPoint == 2)
			{
				emberAfCorePrintln("OFF LED 2");
				turnOffRBGLed(LED2);
				SEND_OnOffStateReport(2,LED_OFF);
			}


			break;
		case ZCL_ON_COMMAND_ID:
			if(endPoint==1)
			{
				emberAfCorePrintln("ON LED 1");
				turnOnLed(LED1,ledBlue);
				SEND_OnOffStateReport(1,LED_ON);
			}else if (endPoint == 2)
			{
				emberAfCorePrintln("ON LED 2");
				turnOnLed(LED2,ledBlue);
				SEND_OnOffStateReport(2,LED_ON);
			}
			break;
		default:
			break;
		}
}


 /* File name:
 *
 * Description:
 *
 *
 * Last Changed By:  $Author: TanPN$
 * Revision:         $Revision: $
 * Last Changed:     $Date: $
 *
 * Code sample:
 ******************************************************************************/
/******************************************************************************/
/*                              INCLUDE FILES                                 */
/******************************************************************************/
#include "af.h"
#include "em_chip.h"
#include "network.h"
#include "Source/App/Send/send.h"
#include "zigbee-framework/zigbee-device-common.h"
/******************************************************************************/
/*                     PRIVATE TYPES and DEFINITIONS                         */
/******************************************************************************/
EmberEventControl joinNetworkEventControl;
EmberEventControl networkLeaveEventControl;

NETWORK_EventHandle_t networkEventHandle;
/******************************************************************************/
/*                     EXPORTED TYPES and DEFINITIONS                         */
/******************************************************************************/

/******************************************************************************/
/*                              PRIVATE DATA                                  */
/******************************************************************************/
uint8_t timeFindAndJoin=0;
static uint8_t timesLeave = 0;
/******************************************************************************/
/*                              EXPORTED DATA                                 */
/******************************************************************************/

/******************************************************************************/
/*                            PRIVATE FUNCTIONS                               */
/******************************************************************************/

/******************************************************************************/
/*                            EXPORTED FUNCTIONS                              */
/******************************************************************************/
void NETWORK_Init(NETWORK_EventHandle_t userNetworkHandle)
{
	networkEventHandle	=userNetworkHandle;
	NETWORK_SetChannelMask(CHANNEL_MASK_DEFAULT);
}

void NETWORK_SetChannelMask(uint16_t channelMask)
{
	uint32_t halChannelMask = 0;

	for(uint8_t i = 0; i < 16; i++){
		if(((channelMask >> i) & 0x01) == 1){
			halChannelMask |= ((1UL) << (i + 11));
		}
	}
	emberSetTxPowerMode(TX_POWER_DEFAULT);
	emAfPluginNetworkSteeringSetChannelMask(halChannelMask, true);
}

/** @brief Stack Status
 *
 * This function is called by the application framework from the stack status
 * handler.  This callbacks provides applications an opportunity to be notified
 * of changes to the stack status and take appropriate action.  The return code
 * from this callback is ignored by the framework.  The framework will always
 * process the stack status after the callback returns.
 *
 * @param status   Ver.: always
 */
boolean emberAfStackStatusCallback(EmberStatus status) {

	EmberNetworkStatus nwkStatusCurrent = emberAfNetworkState();


	if(status == EMBER_NETWORK_UP){

		emberAfCorePrintln("NETWORK_UP %d\n",nwkStatusCurrent);


		if(timeFindAndJoin>0)
		{
			NETWORK_StopFindAndJoin();
			if(networkEventHandle!=NULL)
			{
				networkEventHandle(NETWORK_JOIN_SUCCESS);
			}
		}else
		{
			if(networkEventHandle!=NULL)
			{
				networkEventHandle(NETWORK_HAS_PARENT);
			}
		}
	}else
	{
		emberAfCorePrintln("NETWORK_DOWN %d\n",nwkStatusCurrent);

		if (nwkStatusCurrent == EMBER_NO_NETWORK){
			if(networkEventHandle!=NULL)
			{
				networkEventHandle(NETWORK_OUT_NETWORK);
			}
		}
		else if(nwkStatusCurrent ==  EMBER_JOINED_NETWORK_NO_PARENT){
			networkEventHandle(NETWORK_LOST_PARENT);
		}
	}


	return true;
}

void joinNetworkEventHandle(void)
{
	emberEventControlSetInactive(joinNetworkEventControl);

	if(emberAfNetworkState() == EMBER_NO_NETWORK){

		emberAfPluginNetworkSteeringStart();
		timeFindAndJoin++;
	}
}

void NETWORK_FindAndJoin(void)
{
	if(emberAfNetworkState() == EMBER_NO_NETWORK)
	{
		emberEventControlSetInactive(joinNetworkEventControl);
		emberEventControlSetDelayMS(joinNetworkEventControl,3000);
	}
}

void NETWORK_StopFindAndJoin(void)
{
	emberEventControlSetInactive(joinNetworkEventControl);
}

void NETWORK_Leave(void)
{
	emberEventControlSetInactive(networkLeaveEventControl);
	timesLeave=0;
	emberEventControlSetActive(networkLeaveEventControl);
}

void networkLeaveEventHandle(void)
{
	EmberNetworkStatus nwkStatusCurrent = emberAfNetworkState();
	if( (nwkStatusCurrent != EMBER_NO_NETWORK) && (timesLeave < 5) ){
		uint8_t contents[2];
		contents[1] = 0x00;

		emberSendZigDevRequest(0x0000, LEAVE_RESPONSE, EMBER_AF_DEFAULT_APS_OPTIONS, contents, sizeof(contents));

		/* Send leave request and wait for response 200ms */
		if(timesLeave){
			SendZigDevRequest();
			emberClearBindingTable();
			emberLeaveNetwork(); // Leave network
		}

		timesLeave++;
		emberAfCorePrintln("Leaving network");
		emberEventControlSetDelayMS (networkLeaveEventControl, 1000);
	}
	else{
		halReboot();   // reset
	}
}
/******************************************************************************/

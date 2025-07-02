/*
 * received.c
 *
 *  Created on: Jan 11, 2024
 *      Author: PC
 */
#include "af.h"
#include "em_chip.h"

#include "Source/App/Send/send.h"
#include "received.h"
#include "Source/Mid/Led/Led.h"
#include "Source/Mid/Time/time.h"

uint32_t timeTestRoute;

boolean emberAfPreMessageReceivedCallback(EmberAfIncomingMessage* incomingMessage)
{
	if (incomingMessage->apsFrame->clusterId == ACTIVE_ENDPOINTS_RESPONSE)
	{
	     emberAfCorePrintln("RSSI =%d, TIME_RESPOND= %d\n",incomingMessage->lastHopRssi,TIME_GetElapseTime(timeTestRoute));

	     return true;
	}

	return false;
}

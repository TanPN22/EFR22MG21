/*
 * pir.c
 *
 *  Created on: Jan 15, 2024
 *      Author: PC
 */
#include "af.h"
#include "em_chip.h"
#include "Source/Mid/PIR/pir.h"

pirActionHandle_t pirHardHandle=NULL;
uint8_t pirState;

static boolean 	isMotionSignal(void);
static void 	PIR_INTSignalHandle(uint8_t pin);

EmberEventControl pirDetechEventControl;

void PIR_Init(pirActionHandle_t userPirHandle)
{
	emberAfCorePrintln("PIR Init");
	CMU_ClockEnable(cmuClock_GPIO, true);
	GPIOINT_Init();
    GPIO_PinModeSet(PIR_PORT,
    				PIR_PIN,
					gpioModeInput,
					0);
    /* Register callbacks before setting up and enabling pin interrupt. */
    GPIOINT_CallbackRegister(PIR_PIN,
    						 PIR_INTSignalHandle);
    /* Set rising and falling edge interrupts */

    PIR_Enable(true);
	pirHardHandle=userPirHandle;
}

void PIR_Enable(boolean en)
{
	if(en)
	{
		GPIO_ExtIntConfig(PIR_PORT,PIR_PIN,PIR_PIN,
		                      true,false,true);
	}else
	{
		GPIO_ExtIntConfig(PIR_PORT,PIR_PIN,PIR_PIN,
		                      false,false,false);
	}
}

static boolean isMotionSignal(void)
{
	return (GPIO_PinInGet(PIR_PORT,PIR_PIN)==0) ? false:true;
}

static void PIR_INTSignalHandle(uint8_t pin)
{

	if(pin != PIR_PIN)
	{
		return;
	}

	if(isMotionSignal())
	{
		pirState=PIR_STATE_DEBOUNCE;
		PIR_Enable(false);

		emberEventControlSetInactive(pirDetechEventControl);
		emberEventControlSetDelayMS(pirDetechEventControl,200);
	}
}

void pirDetechEventHandle(void)
{
	emberEventControlSetInactive(pirDetechEventControl);

	switch(pirState)
	{
		case PIR_STATE_DEBOUNCE:

			if(isMotionSignal())
			{
				emberAfCorePrintln("PIR_DETECH_MOTION");
				pirState=PIR_STATE_WAIT_5S;
				if(pirHardHandle!=NULL)
				{

					pirHardHandle(PIR_MOTION);
				}
				emberEventControlSetDelayMS(pirDetechEventControl,5000);

			}else
			{
				PIR_Enable(true);
			}
			break;
		case PIR_STATE_WAIT_5S:
			{
				pirState=PIR_STATE_WAIT_30S;
				PIR_Enable(true);
				emberEventControlSetDelayMS(pirDetechEventControl,30000);
			}
			break;
		case PIR_STATE_WAIT_30S:
			{
				if(pirHardHandle!=NULL)
				{
					emberAfCorePrintln("PIR_DETECH_UNMOTION");
					pirHardHandle(PIR_UNMOTION);
				}
			}
			break;
		default:
			break;
	}
}

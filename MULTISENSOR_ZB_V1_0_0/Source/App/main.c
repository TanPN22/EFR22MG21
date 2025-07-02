/*
 * main.c
 *
 *  Created on: Dec 28, 2023
 *      Author: PC
 */

//________________INC_______________
#include "app/framework/include/af.h"
#include "Source/Mid/Button/button.h"
#include "Source/Mid/Kalman_filter/kalman_filter.h"
#include "Source/Mid/Led/led.h"
#include "Source/Mid/LDR/ldr.h"
#include "Source/Mid/Temphumi/Si7020.h"
#include "em_chip.h"

//_________________DEF_____________
/* define ------------------------------------------------------------*/
#define PERIOD_SCAN_SENSORLIGHT									5000 	//	ms
#define PERIOD_SCAN_SENSORTEMHUMI								10000	//	ms

uint32_t KalmanHumi=0;
uint32_t KalmanTemp=0;
/* Function prototypes -----------------------------------------------*/
//void User_buttonPressAndHoldEventHandler(uint8_t button, BUTTON_Event_t pressAndHoldEvent);
//void User_buttonPressAndHoldingEventHandler(uint8_t button, BUTTON_Event_t holdingHandler);
/* Event **************************************************************/
EmberEventControl readValueSensorLightControl;
EmberEventControl ReadValueTempHumiControl;
//________________FUNC_____________
/** @brief Main Init
 *
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
	LDRInit();
	initI2C();
	Si7020_Init();
	KalmanFilterInit(2, 2, 0.001); // Initialize Kalman filter
	emberEventControlSetDelayMS(readValueSensorLightControl, 1000);
	emberEventControlSetDelayMS(ReadValueTempHumiControl,1000);
//	ledInit();
//	buttonInit(Main_ButtonHoldCallbackHandler, Main_ButtonPressCallbackHandler);
}

/****************************EVENT HANDLER MIDDER********************************************************************/
/*
 * @func	User_buttonPressAndHoldingEventHandler
 * @brief	Event Button Handler
 * @param	button, holdingHandler
 * @retval	None
 */
//void User_buttonPressAndHoldingEventHandler(uint8_t button, BUTTON_Event_t holdingHandler)
//{
//	switch(holdingHandler)
//	{
//	case hold_1s:
//		emberAfCorePrintln("SW1: 1 s");
//		break;
//	case hold_2s:
//		emberAfCorePrintln("SW1: 2 s");
//		break;
//	case hold_3s:
//		emberAfCorePrintln("SW1: 3 s");
//		break;
//
//	default:
//
//		break;
//	}
//}



/**
 * @func   LightSensor_AdcPollingReadHandler
 * @brief  Read value from ADC
 * @param  None
 * @retval None
 */
void LightSensor_AdcPollingReadHandler(void)
{
	emberEventControlSetInactive(readValueSensorLightControl);
	uint32_t lux = LightSensor_AdcPollingRead();
	emberAfCorePrintln("Light:   %d lux         ",lux);
	emberEventControlSetDelayMS(readValueSensorLightControl,PERIOD_SCAN_SENSORLIGHT);
}

/**
 * @func    ReadValueTempHumiHandler
 * @brief   Event Sensor Handler
 * @param   None
 * @retval  None
 */
void ReadValueTempHumiHandler(void)
{
	emberEventControlSetInactive(ReadValueTempHumiControl);
	KalmanHumi = Si7020_MeasureHumi();
	KalmanTemp = Si7020_MeasureTemp();
	emberAfCorePrintln("Humi:    %d RH       Temp:     %d oC        ", KalmanHumi,KalmanTemp);
	emberEventControlSetDelayMS(ReadValueTempHumiControl,PERIOD_SCAN_SENSORTEMHUMI);
}

/*
 * @func	Main_ButtonPressCallbackHandler
 * @brief	Event Button Handler
 * @param	button, pressHandler
 * @retval	None
 */
void Main_ButtonPressCallbackHandler(uint8_t button, BUTTON_Event_t pressHandler)
{
//	switch(pressHandler)
//		{
//		case press_1:
//			if(button == SW_1)
//			{
//				emberAfCorePrintln("SW1: 1 time");
//				turnOnLed(LED1,ledRed);
//			}
//			else
//			{
//				emberAfCorePrintln("SW2: 1 time");
//				toggleLed(LED2, ledPink,3,300,300);
//
//			}
//		break;
//		case press_2:
//			if(button == SW_1)
//			{
//				emberAfCorePrintln("SW1: 2 times");
//				turnOnLed(LED1,ledGreen);
//
//			}
//			else
//			{
//				emberAfCorePrintln("SW2: 2 time");
//				toggleLed(LED2, ledyellow,4,300,300);
//
//			}
//			break;
//		case press_3:
//			if(button == SW_1)
//			{
//				emberAfCorePrintln("SW1: 3 time");
//				turnOnLed(LED1,ledBlue);
//
//
//			}
//			else
//			{
//				emberAfCorePrintln("SW2: 3 time");
//			}
//			break;
//		case press_4:
//			if(button == SW_1)
//			{
//				emberAfCorePrintln("SW1: 4 time");
//
//
//			}
//			else
//			{
//				emberAfCorePrintln("SW2: 4 time");
//			}
//			break;
//		case press_5:
//			if(button == SW_1)
//			{
//				emberAfCorePrintln("SW1: 5 time");
//
//			}
//			else
//			{
//				emberAfCorePrintln("SW2: 5 time");
//			}
//			break;
//		default:
//			break;
//		}
}

/*
 * @func	Main_ButtonHoldCallbackHandler
 * @brief	Event Button Handler
 * @param	button, holdingHandler
 * @retval	None
 */
void Main_ButtonHoldCallbackHandler(uint8_t button, BUTTON_Event_t holdingHandler)
{
//	emberAfCorePrintln("SW %d HOLDING %d s\n",button+1,holdingHandler-press_max);
//	switch(holdingHandler)
//	{
//	case hold_1s:
//		emberAfCorePrintln("SW1: 1 s");
//		break;
//	case hold_2s:
//		emberAfCorePrintln("SW1: 2 s");
//		break;
//	case hold_3s:
//		emberAfCorePrintln("SW1: 3 s");
//		break;
//	case hold_4s:
//		emberAfCorePrintln("SW1: 4 s");
//		break;
//	case hold_5s:
//		emberAfCorePrintln("SW1: 5 s");
//		break;
//
//	default:
//		break;
//	}
}

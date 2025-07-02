/*
 * pir.h
 *
 *  Created on: Jan 15, 2024
 *      Author: PC
 */

#ifndef SOURCE_MID_PIR_PIR_H_
#define SOURCE_MID_PIR_PIR_H_

#include "stdbool.h"
#include "stddef.h"
#include "em_cmu.h"
#include "em_gpio.h"

#define PIR_PORT			gpioPortC
#define PIR_PIN				(4U)

typedef enum
{
	PIR_MOTION,
	PIR_UNMOTION
}pirAction_t;

enum
{
	PIR_STATE_DEBOUNCE,
	PIR_STATE_WAIT_5S,
	PIR_STATE_WAIT_30S,
};

typedef void (*pirActionHandle_t)(pirAction_t action);

void PIR_Init(pirActionHandle_t userPirHandle);
void PIR_Enable(boolean en);
#endif /* SOURCE_MID_PIR_PIR_H_ */

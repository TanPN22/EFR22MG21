/*
 * button.h
 *
 *  Created on: Dec 26, 2023
 *      Author: PC
 */

#ifndef SOURCE_MID_BUTTON_BUTTON_H_
#define SOURCE_MID_BUTTON_BUTTON_H_

typedef enum{
	release,
	press_1,
	press_2,
	press_3,
	press_4,
	hold_1s,
	hold_2s,
}Btnstate;

typedef void (*buttonCallbackFunction) (uint8_t, Btnstate);

void buttonInit(buttonCallbackFunction);

#endif /* SOURCE_MID_BUTTON_BUTTON_H_ */

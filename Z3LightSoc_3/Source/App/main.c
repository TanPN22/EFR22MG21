/*
 * main.c
 *
 *  Created on: Dec 26, 2023
 *      Author: PC
 */

#include "af.h"
#include "Source/Mid/button/button.h"

void buttonCallbackHandler(uint8_t button, Btnstate state);

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
	buttonInit(buttonCallbackHandler);
}

void buttonCallbackHandler(uint8_t button, Btnstate state)
{
	if (button == BUTTON0)
	{
		switch (state) {
			case release:
				emberAfCorePrintln("SW1 is Released");
				break;
			case press_1:
				emberAfCorePrintln("SW1 is Pressed");
				break;
			default:
				break;
		}
	}else if (button == BUTTON1)
	{
		switch (state) {
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

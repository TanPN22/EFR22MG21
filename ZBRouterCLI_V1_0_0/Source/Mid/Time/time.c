/*
 * Time.c
 *
 *  Created on: October 20, 2019
 *      Author: LongHD
 */

/******************************************************************************/

/******************************************************************************/
/*                              INCLUDE FILES                                 */
/******************************************************************************/

#include "af.h"
#include "Time.h"

/******************************************************************************/
/*                     EXPORTED TYPES and DEFINITIONS                         */
/******************************************************************************/



/******************************************************************************/
/*                              PRIVATE DATA                                  */
/******************************************************************************/



/******************************************************************************/
/*                              EXPORTED DATA                                 */
/******************************************************************************/



/******************************************************************************/
/*                            FUNCTIONS                                       */
/******************************************************************************/



/******************************************************************************/

/**
 * @function :  TIME_ResetTime
 * @brief    :  reset time
 * @parameter:  time
 * @retVal   :  None
 */

void TIME_ResetTime (uint32_t* time){
	*time = halCommonGetInt32uMillisecondTick();
}

/**
 * @function :  TIME_GetElapseTime
 * @brief    :  Return elapse time
 * @parameter:  Time start
 * @retVal   :  Elapse time
 */

uint32_t TIME_GetElapseTime (uint32_t timeStart){
	uint32_t currentTime = halCommonGetInt32uMillisecondTick();
	if(timeStart <= currentTime){
		return (currentTime - timeStart);
	}
	else {
		return (0xFFFFFFFF - timeStart + currentTime);
	}
}

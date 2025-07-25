/*
 * Time.h
 *
 *  Created on: October 20, 2019
 *      Author: LongHD
 */

#ifndef SOURCE_HARD_TIME_TIME_H_
#define SOURCE_HARD_TIME_TIME_H_

/******************************************************************************/

/******************************************************************************/
/*                              INCLUDE FILES                                 */
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



/******************************************************************************/
/*                            FUNCTIONS                                       */
/******************************************************************************/

void     TIME_ResetTime (uint32_t* time);
uint32_t TIME_GetElapseTime (uint32_t timeStart);

/******************************************************************************/

#endif /* SOURCE_HARD_TIME_TIME_H_ */

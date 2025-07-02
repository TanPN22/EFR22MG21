/*
 * network.h
 *
 *  Created on: Jan 9, 2024
 *      Author: PC
 */

#ifndef SOURCE_APP_NETWORK_NETWORK_H_
#define SOURCE_APP_NETWORK_NETWORK_H_

/*******************************************************************************/
/******************************************************************************/
/*                              INCLUDE FILES                                 */
/******************************************************************************/

/******************************************************************************/
/*                     PRIVATE TYPES and DEFINITIONS                         */
/******************************************************************************/
#define PAGE_CHANNEL_FIND_DEFAULT          0
#define TX_POWER_DEFAULT                   10
#define CHANNEL_MASK_DEFAULT               (0x7FFF)
/******************************************************************************/
/*                     EXPORTED TYPES and DEFINITIONS                         */
/******************************************************************************/
typedef void (*NETWORK_EventHandle_t)(uint8_t state);

enum
{
    NETWORK_JOIN_SUCCESS,
    NETWORK_JOIN_FAIL,
    NETWORK_HAS_PARENT,
    NETWORK_LOST_PARENT,
    NETWORK_OUT_NETWORK,
};

/******************************************************************************/
/*                              PRIVATE DATA                                  */
/******************************************************************************/

/******************************************************************************/
/*                              EXPORTED DATA                                 */
/******************************************************************************/

/******************************************************************************/
/*                            PRIVATE FUNCTIONS                               */
/******************************************************************************/
void NETWORK_Init(NETWORK_EventHandle_t userNetworkHandle);
void NETWORK_SetChannelMask(uint16_t channelMask);
void NETWORK_FindAndJoin(void);
void NETWORK_StopFindAndJoin(void);
void NETWORK_Leave(void);
/******************************************************************************/
/*                            EXPORTED FUNCTIONS                              */
/******************************************************************************/

/******************************************************************************/

#endif /* SOURCE_APP_NETWORK_NETWORK_H_ */

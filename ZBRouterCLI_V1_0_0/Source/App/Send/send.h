/*
 * send.h
 *
 *  Created on: Jan 10, 2024
 *      Author: PC
 */

#ifndef SOURCE_APP_SEND_SEND_H_
#define SOURCE_APP_SEND_SEND_H_

#define MAX_DATA_COMMAND_SIZE                  50

#define SOURCE_ENDPOINT_PRIMARY                1
#define DESTINATION_ENDPOINT                   1
#define HC_NETWORK_ADDRESS                     0x0000

void SEND_ReportInfoToHc(void);
void SEND_OnOffStateReport(uint8_t endpoint, uint8_t value);
void SEND_OnOffToGroup(uint8_t localEndpoint, uint8_t remoteEndpoint, bool value, uint16_t nodeID);

#endif /* SOURCE_APP_SEND_SEND_H_ */

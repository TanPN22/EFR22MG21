 /* File name: network.c
 *
 * Description:
 *
 *
 * Last Changed By:  $Author: TanPN$
 * Revision:         $Revision: $
 * Last Changed:     $Date: $
 *
 * Code sample:
 ******************************************************************************/
/******************************************************************************/
/*                              INCLUDE FILES                                 */
/******************************************************************************/
#include "app/framework/include/af.h"
#include "network.h"
#include "app/framework/cli/network-cli.h"
/******************************************************************************/
/*                     PRIVATE TYPES and DEFINITIONS                         */
/******************************************************************************/
/******************************************************************************/
/*                     EXPORTED TYPES and DEFINITIONS                         */
/******************************************************************************/
void NetworkInit(void)
{
	emberAfCorePrintln("Network create");

	EmberStatus status;
	EmberNetworkParameters networkParameters;


	networkParameters.panId = 0x2210;
	networkParameters.radioTxPower = 10;
	networkParameters.channels = 5;

	initNetworkParams(&networkParameters);
	status = emberAfFormNetwork(&networkParameters);
	emberAfAppPrintln("%p 0x%x", "form", status);
	emberAfAppFlush();

	emberNetworkInit(&status);

	emberAfCorePrintln("Extended PAN ID: %d", networkParameters.extendedPanId);
	emberAfCorePrintln("PAN ID: %d\n", networkParameters.panId);
	emberAfCorePrintln("Radio Tx Power: %d dBm\n", networkParameters.radioTxPower);
	emberAfCorePrintln("Radio Channel: %d\n", networkParameters.radioChannel);
	emberAfCorePrintln("Join Method: %d\n", networkParameters.joinMethod);
	emberAfCorePrintln("NWK Manager ID: %d\n", networkParameters.nwkManagerId);
	emberAfCorePrintln("NWK Update ID: %d\n", networkParameters.nwkUpdateId);
	emberAfCorePrintln("Channels: %d\n", networkParameters.channels);
}

/******************************************************************************/
/*                              PRIVATE DATA                                  */
/******************************************************************************/

/******************************************************************************/
/*                              EXPORTED DATA                                 */
/******************************************************************************/

/******************************************************************************/
/*                            PRIVATE FUNCTIONS                               */
/******************************************************************************/

/******************************************************************************/
/*                            EXPORTED FUNCTIONS                              */
/******************************************************************************/

/******************************************************************************/



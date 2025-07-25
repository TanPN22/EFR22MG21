#ifndef HAL_CONFIG_H
#define HAL_CONFIG_H

#include "em_device.h"
#include "hal-config-types.h"

// This file is auto-generated by Hardware Configurator in Simplicity Studio.
// Any content between $[ and ]$ will be replaced whenever the file is regenerated.
// Content outside these regions will be preserved.

// $[ACMP0]
// [ACMP0]$

// $[ACMP1]
// [ACMP1]$

// $[ADC0]
// [ADC0]$

// $[ANTDIV]
// [ANTDIV]$

// $[BATTERYMON]
// [BATTERYMON]$

// $[BTL_BUTTON]
// [BTL_BUTTON]$

// $[BULBPWM]
// [BULBPWM]$

// $[BULBPWM_COLOR]
// [BULBPWM_COLOR]$

// $[BUTTON]
// [BUTTON]$

// $[CMU]
#define HAL_CLK_HFCLK_SOURCE            (HAL_CLK_HFCLK_SOURCE_HFRCO)
#define HAL_CLK_LFACLK_SOURCE           (HAL_CLK_LFCLK_SOURCE_DISABLED)
#define HAL_CLK_LFBCLK_SOURCE           (HAL_CLK_LFCLK_SOURCE_DISABLED)
#define HAL_CLK_LFECLK_SOURCE           (HAL_CLK_LFCLK_SOURCE_DISABLED)
#define BSP_CLK_HFXO_PRESENT            (1)
#define BSP_CLK_HFXO_FREQ               (38400000UL)
#define BSP_CLK_HFXO_INIT                CMU_HFXOINIT_DEFAULT
#define HAL_CLK_HFXO_AUTOSTART          (HAL_CLK_HFXO_AUTOSTART_NONE)
#define BSP_CLK_HFXO_CTUNE              (346)
#define BSP_CLK_LFXO_PRESENT            (1)
#define BSP_CLK_LFXO_INIT                CMU_LFXOINIT_DEFAULT
#define BSP_CLK_LFXO_FREQ               (32768U)
#define BSP_CLK_LFXO_CTUNE              (32U)
// [CMU]$

// $[COEX]
// [COEX]$

// $[CS5463]
// [CS5463]$

// $[CSEN]
// [CSEN]$

// $[DCDC]
#define BSP_DCDC_PRESENT                (1)

#define BSP_DCDC_INIT                    EMU_DCDCINIT_DEFAULT
#define HAL_DCDC_BYPASS                 (0)
// [DCDC]$

// $[EMU]
// [EMU]$

// $[EXTFLASH]
// [EXTFLASH]$

// $[EZRADIOPRO]
// [EZRADIOPRO]$

// $[FEM]
// [FEM]$

// $[GPIO]
// [GPIO]$

// $[I2C0]
// [I2C0]$

// $[I2C1]
// [I2C1]$

// $[I2CSENSOR]
// [I2CSENSOR]$

// $[IDAC0]
// [IDAC0]$

// $[IOEXP]
// [IOEXP]$

// $[LED]
// [LED]$

// $[LESENSE]
// [LESENSE]$

// $[LETIMER0]
// [LETIMER0]$

// $[LEUART0]
// [LEUART0]$

// $[LFXO]
// [LFXO]$

// $[MODEM]
// [MODEM]$

// $[PA]
// [PA]$

// $[PCNT0]
// [PCNT0]$

// $[PORTIO]
// [PORTIO]$

// $[PRS]
// [PRS]$

// $[PTI]
// [PTI]$

// $[PYD1698]
// [PYD1698]$

// $[SERIAL]
// [SERIAL]$

// $[SPIDISPLAY]
// [SPIDISPLAY]$

// $[SPINCP]
// [SPINCP]$

// $[TIMER0]
// [TIMER0]$

// $[TIMER1]
// [TIMER1]$

// $[UARTNCP]
// [UARTNCP]$

// $[USART0]
// [USART0]$

// $[USART1]
// [USART1]$

// $[USART2]
// [USART2]$

// $[VCOM]
// [VCOM]$

// $[VDAC0]
// [VDAC0]$

// $[VUART]
// [VUART]$

// $[WDOG]
// [WDOG]$

// $[WTIMER0]
// [WTIMER0]$

#if defined(_SILICON_LABS_MODULE)
#include "sl_module.h"
#endif


#endif /* HAL_CONFIG_H */


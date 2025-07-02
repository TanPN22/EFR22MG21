################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7/platform/bootloader/driver/btl_driver_euart.c \
D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7/platform/bootloader/driver/btl_driver_uart.c 

OBJS += \
./uart-driver/btl_driver_euart.o \
./uart-driver/btl_driver_uart.o 

C_DEPS += \
./uart-driver/btl_driver_euart.d \
./uart-driver/btl_driver_uart.d 


# Each subdirectory must supply rules for building sources it contributes
uart-driver/btl_driver_euart.o: D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7/platform/bootloader/driver/btl_driver_euart.c
	@echo 'Building file: $<'
	@echo 'Invoking: GNU ARM C Compiler'
	arm-none-eabi-gcc -g3 -gdwarf-2 -mcpu=cortex-m33 -mthumb -std=c99 '-DEFR32MG21A010F512IM32=1' '-DBTL_CONFIG_FILE="bootloader-configuration.h"' '-DBTL_SLOT_CONFIGURATION="bootloader-slot-configuration.h"' '-DSL_RAMFUNC_DISABLE=1' '-DBOOTLOADER_VERSION_MAIN_CUSTOMER=3' '-DMBEDTLS_CONFIG_FILE="config-sl-crypto-all-acceleration.h"' '-DUSE_SE_IN_IRQ=1' '-DHAL_CONFIG=1' '-DEMBER_AF_USE_HWCONF=1' '-D__STARTUP_CLEAR_BSS=1' '-D__START=main' '-DBOOTLOADER_SECOND_STAGE=1' -I"D:\DH\Lumi\Zigbee\SimplicityStudio\SimplicityStudio\MyWorkspace\ZB_NCP_Bootloader" -I"D:\DH\Lumi\Zigbee\SimplicityStudio\SimplicityStudio\MyWorkspace\ZB_NCP_Bootloader\hal-config" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7///platform/Device/SiliconLabs/EFR32MG21/Include" -I"D:\DH\Lumi\Zigbee\SimplicityStudio\SimplicityStudio\MyWorkspace\ZB_NCP_Bootloader\hal-config" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/bootloader/." -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/emdrv/common/inc" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/emlib/inc" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//util/third_party/mbedtls/configs" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//util/third_party/mbedtls/include" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//util/third_party/mbedtls/sl_crypto/include" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//util/third_party/mbedtls/sl_crypto/src/cryptoacc/include" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//util/third_party/mbedtls/sl_crypto/src/cryptoacc/src" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/CMSIS/Include" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//hardware/module/config" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/halconfig/inc/hal-config" -Os -Wall -Wextra -Werror -c -fmessage-length=0 -ffunction-sections -fdata-sections -mfpu=fpv5-sp-d16 -mfloat-abi=softfp -MMD -MP -MF"uart-driver/btl_driver_euart.d" -MT"uart-driver/btl_driver_euart.o" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

uart-driver/btl_driver_uart.o: D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7/platform/bootloader/driver/btl_driver_uart.c
	@echo 'Building file: $<'
	@echo 'Invoking: GNU ARM C Compiler'
	arm-none-eabi-gcc -g3 -gdwarf-2 -mcpu=cortex-m33 -mthumb -std=c99 '-DEFR32MG21A010F512IM32=1' '-DBTL_CONFIG_FILE="bootloader-configuration.h"' '-DBTL_SLOT_CONFIGURATION="bootloader-slot-configuration.h"' '-DSL_RAMFUNC_DISABLE=1' '-DBOOTLOADER_VERSION_MAIN_CUSTOMER=3' '-DMBEDTLS_CONFIG_FILE="config-sl-crypto-all-acceleration.h"' '-DUSE_SE_IN_IRQ=1' '-DHAL_CONFIG=1' '-DEMBER_AF_USE_HWCONF=1' '-D__STARTUP_CLEAR_BSS=1' '-D__START=main' '-DBOOTLOADER_SECOND_STAGE=1' -I"D:\DH\Lumi\Zigbee\SimplicityStudio\SimplicityStudio\MyWorkspace\ZB_NCP_Bootloader" -I"D:\DH\Lumi\Zigbee\SimplicityStudio\SimplicityStudio\MyWorkspace\ZB_NCP_Bootloader\hal-config" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7///platform/Device/SiliconLabs/EFR32MG21/Include" -I"D:\DH\Lumi\Zigbee\SimplicityStudio\SimplicityStudio\MyWorkspace\ZB_NCP_Bootloader\hal-config" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/bootloader/." -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/emdrv/common/inc" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/emlib/inc" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//util/third_party/mbedtls/configs" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//util/third_party/mbedtls/include" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//util/third_party/mbedtls/sl_crypto/include" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//util/third_party/mbedtls/sl_crypto/src/cryptoacc/include" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//util/third_party/mbedtls/sl_crypto/src/cryptoacc/src" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/CMSIS/Include" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//hardware/module/config" -I"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/halconfig/inc/hal-config" -Os -Wall -Wextra -Werror -c -fmessage-length=0 -ffunction-sections -fdata-sections -mfpu=fpv5-sp-d16 -mfloat-abi=softfp -MMD -MP -MF"uart-driver/btl_driver_uart.d" -MT"uart-driver/btl_driver_uart.o" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '



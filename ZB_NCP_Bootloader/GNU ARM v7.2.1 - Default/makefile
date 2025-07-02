################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include xmodem-uart/subdir.mk
-include uart-driver/subdir.mk
-include token-management/subdir.mk
-include parser/subdir.mk
-include mbedtls/subdir.mk
-include gpio-activation/subdir.mk
-include emlib/subdir.mk
-include delay-driver/subdir.mk
-include crypto/subdir.mk
-include crc/subdir.mk
-include core/EFR32/gcc/subdir.mk
-include core/subdir.mk
-include CMSIS/subdir.mk
-include subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 

# All Target
all: ZB_NCP_Bootloader.axf

# Tool invocations
ZB_NCP_Bootloader.axf: $(OBJS) $(USER_OBJS)
	@echo 'Building target: $@'
	@echo 'Invoking: GNU ARM C Linker'
	arm-none-eabi-gcc -g3 -gdwarf-2 -mcpu=cortex-m33 -mthumb -T "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/bootloader/core/GCC/main_btl_main_flash_se.ld" -Xlinker --gc-sections -Xlinker -Map="ZB_NCP_Bootloader.map" -mfpu=fpv5-sp-d16 -mfloat-abi=softfp --specs=nano.specs -o ZB_NCP_Bootloader.axf -Wl,--start-group "./CMSIS/system_efr32mg21.o" "./bootloader-callback-stubs.o" "./bootloader-callbacks.o" "./core/EFR32/gcc/main_btl_startup.o" "./core/btl_core.o" "./core/btl_driver_util.o" "./core/btl_main.o" "./crc/btl_crc16.o" "./crc/btl_crc32.o" "./crypto/btl_security_aes.o" "./crypto/btl_security_ecdsa.o" "./crypto/btl_security_sha256.o" "./crypto/ecc.o" "./delay-driver/btl_driver_delay.o" "./emlib/em_assert.o" "./emlib/em_cmu.o" "./emlib/em_core.o" "./emlib/em_crypto.o" "./emlib/em_emu.o" "./emlib/em_eusart.o" "./emlib/em_gpio.o" "./emlib/em_msc.o" "./emlib/em_rmu.o" "./emlib/em_se.o" "./emlib/em_system.o" "./emlib/em_timer.o" "./emlib/em_usart.o" "./emlib/em_wdog.o" "./gpio-activation/btl_gpio_activation.o" "./mbedtls/crypto_aes.o" "./mbedtls/crypto_management.o" "./mbedtls/crypto_sha.o" "./mbedtls/cryptoacc_aes.o" "./mbedtls/cryptoacc_management.o" "./mbedtls/cryptoacc_sha.o" "./mbedtls/se_aes.o" "./mbedtls/se_management.o" "./mbedtls/se_sha.o" "./mbedtls/shax.o" "./parser/btl_gbl_custom_tags.o" "./parser/btl_image_parser.o" "./token-management/btl_security_tokens.o" "./uart-driver/btl_driver_euart.o" "./uart-driver/btl_driver_uart.o" "./xmodem-uart/btl_comm_xmodem.o" "./xmodem-uart/btl_xmodem.o" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/bootloader/build/lib/libbootloader_efr32xg21_gcc.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/bootloader/build/lib/libparser_efr32xg21_gcc.a" -lnosys -Wl,--end-group -Wl,--start-group -lgcc -lc -lnosys -Wl,--end-group
	@echo 'Finished building target: $@'
	@echo ' '

	@echo 'Building hex file: ZB_NCP_Bootloader.hex'
	arm-none-eabi-objcopy -O ihex "ZB_NCP_Bootloader.axf" "ZB_NCP_Bootloader.hex"
	@echo ' '

	@echo 'Building bin file: ZB_NCP_Bootloader.bin'
	arm-none-eabi-objcopy -O binary "ZB_NCP_Bootloader.axf" "ZB_NCP_Bootloader.bin"
	@echo ' '

	@echo 'Building s37 file: ZB_NCP_Bootloader.s37'
	arm-none-eabi-objcopy -O srec "ZB_NCP_Bootloader.axf" "ZB_NCP_Bootloader.s37"
	@echo ' '

	@echo 'Running size tool'
	arm-none-eabi-size "ZB_NCP_Bootloader.axf" -A
	@echo ' '

	$(MAKE) --no-print-directory post-build

# Other Targets
clean:
	-$(RM) $(EXECUTABLES)$(OBJS)$(C_DEPS) ZB_NCP_Bootloader.axf
	-@echo ' '

post-build:
	-sh "D:\DH\Lumi\Zigbee\SimplicityStudio\SimplicityStudio\MyWorkspace\ZB_NCP/ZB_NCP_postbuild.sh" ZB_NCP_Bootloader
	-@echo ' '

.PHONY: all clean dependents
.SECONDARY: post-build

-include ../makefile.targets

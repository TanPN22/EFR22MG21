################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include zcl-framework-core/subdir.mk
-include update-tc-link-key/subdir.mk
-include strong-random/subdir.mk
-include simple-main/subdir.mk
-include serial/EFR32/subdir.mk
-include serial/subdir.mk
-include scan-dispatch/subdir.mk
-include reporting/subdir.mk
-include nvm3/EFR32/subdir.mk
-include nvm3/subdir.mk
-include network-steering/subdir.mk
-include mbedtls/EFR32/subdir.mk
-include interpan/subdir.mk
-include identify/subdir.mk
-include heartbeat/subdir.mk
-include hal-library/EFR32/subdir.mk
-include find-and-bind-target/subdir.mk
-include end-device-support/subdir.mk
-include emlib/subdir.mk
-include emdrv/subdir.mk
-include ember-minimal-printf/subdir.mk
-include efr32/subdir.mk
-include debug-jtag/EFR32/subdir.mk
-include debug-basic-library/EFR32/subdir.mk
-include counters/subdir.mk
-include coexistence-stub/EFR32/subdir.mk
-include ccm-encryption/subdir.mk
-include basic/subdir.mk
-include antenna-stub/subdir.mk
-include aes-cmac/subdir.mk
-include adc/EFR32/subdir.mk
-include Source/Mid/Time/subdir.mk
-include Source/Mid/TempHumi/subdir.mk
-include Source/Mid/PIR/subdir.mk
-include Source/Mid/LED/subdir.mk
-include Source/Mid/LDR/subdir.mk
-include Source/Mid/Kalman_filter/subdir.mk
-include Source/Mid/Button/subdir.mk
-include Source/App/main/subdir.mk
-include Source/App/Send/subdir.mk
-include Source/App/Received/subdir.mk
-include Source/App/Network/subdir.mk
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
all: pre-build main-build

# Main-build Target
main-build: ZB_SZEDCLI_V1_0_0.axf

# Tool invocations
ZB_SZEDCLI_V1_0_0.axf: $(OBJS) $(USER_OBJS)
	@echo 'Building target: $@'
	@echo 'Invoking: GNU ARM C Linker'
	arm-none-eabi-gcc -g3 -gdwarf-2 -mcpu=cortex-m33 -mthumb -T "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/base/hal/micro/cortexm3/efm32/gcc-cfg.ld" -L"D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/base/hal/micro/cortexm3/" -Xlinker --defsym=FLASH_SIZE=524288 -Xlinker --defsym=RAM_SIZE=65536 -Xlinker --defsym=FLASH_PAGE_SIZE=8192 -Xlinker --defsym=SIMEEPROM_SIZE=32768 -Xlinker --defsym=PSSTORE_SIZE=0 -Xlinker --defsym=LONGTOKEN_SIZE=0 -Xlinker --defsym=HEADER_SIZE=512 -Xlinker --defsym=BTL_SIZE=16384 -Xlinker --defsym=LOCKBITS_IN_MAINFLASH_SIZE=8192 -Xlinker --defsym=NULL_BTL=1 -Xlinker --defsym=EMBER_MALLOC_HEAP_SIZE=0 -Xlinker --gc-sections -Xlinker -Map="ZB_SZEDCLI_V1_0_0.map" -mfpu=fpv5-sp-d16 -mfloat-abi=hard --specs=nano.specs -o ZB_SZEDCLI_V1_0_0.axf -Wl,--start-group "./Source/App/Network/network.o" "./Source/App/Received/received.o" "./Source/App/Send/send.o" "./Source/App/main/main.o" "./Source/Mid/Button/Button.o" "./Source/Mid/Kalman_filter/kalman_filter.o" "./Source/Mid/LDR/ldr.o" "./Source/Mid/LED/led.o" "./Source/Mid/PIR/pir.o" "./Source/Mid/TempHumi/SI7020.o" "./Source/Mid/Time/time.o" "./ZB_SZEDCLI_V1_0_0_callbacks.o" "./call-command-handler.o" "./callback-stub.o" "./command-interpreter2.o" "./crc.o" "./ember-base-configuration.o" "./ember-configuration.o" "./endian.o" "./library.o" "./mem-util.o" "./random.o" "./security-address-cache.o" "./stack-handler-stub.o" "./token-def.o" "./zigbee-device-common.o" "./zigbee-device-library.o" "./znet-bookkeeping.o" "./znet-cli.o" "./adc/EFR32/adc-efr32.o" "./aes-cmac/aes-cmac.o" "./antenna-stub/antenna-stub.o" "./basic/basic.o" "./ccm-encryption/ccm-star.o" "./coexistence-stub/EFR32/coexistence-802154.o" "./coexistence-stub/EFR32/coulomb-counter-802154.o" "./counters/counters-cli.o" "./counters/counters-ota.o" "./counters/counters-soc.o" "./debug-basic-library/EFR32/SEGGER_RTT.o" "./debug-jtag/EFR32/debug-jtag-efr32.o" "./efr32/assert-crash-handlers.o" "./efr32/button.o" "./efr32/buzzer-efr32.o" "./efr32/cstartup-common.o" "./efr32/diagnostic.o" "./efr32/ext-device.o" "./efr32/faults-v7m.o" "./efr32/isr-stubs.o" "./efr32/led.o" "./efr32/mfg-token.o" "./efr32/micro-common.o" "./efr32/micro.o" "./efr32/sleep-efm32.o" "./efr32/token.o" "./ember-minimal-printf/ember-printf.o" "./emdrv/dmadrv.o" "./emdrv/gpiointerrupt.o" "./emdrv/sl_sleeptimer.o" "./emdrv/sl_sleeptimer_hal_rtcc.o" "./emdrv/sleep.o" "./emdrv/tempdrv.o" "./emdrv/uartdrv.o" "./emdrv/ustimer.o" "./emlib/em_adc.o" "./emlib/em_cmu.o" "./emlib/em_core.o" "./emlib/em_cryotimer.o" "./emlib/em_emu.o" "./emlib/em_eusart.o" "./emlib/em_gpio.o" "./emlib/em_i2c.o" "./emlib/em_iadc.o" "./emlib/em_ldma.o" "./emlib/em_leuart.o" "./emlib/em_msc.o" "./emlib/em_prs.o" "./emlib/em_rmu.o" "./emlib/em_rtcc.o" "./emlib/em_se.o" "./emlib/em_system.o" "./emlib/em_timer.o" "./emlib/em_usart.o" "./emlib/em_wdog.o" "./emlib/system_efr32mg21.o" "./end-device-support/end-device-move.o" "./end-device-support/end-device-support-cli.o" "./end-device-support/end-device-support.o" "./end-device-support/polling-common.o" "./end-device-support/polling-soc.o" "./find-and-bind-target/find-and-bind-target-cli.o" "./find-and-bind-target/find-and-bind-target.o" "./hal-library/EFR32/hal-config-gpio.o" "./hal-library/EFR32/hal-config.o" "./hal-library/EFR32/sl_mpu.o" "./heartbeat/heartbeat.o" "./identify/identify-cli.o" "./identify/identify.o" "./interpan/interpan-cli.o" "./interpan/interpan-soc.o" "./interpan/interpan.o" "./mbedtls/EFR32/aes.o" "./mbedtls/EFR32/aes_aes.o" "./mbedtls/EFR32/aesni.o" "./mbedtls/EFR32/arc4.o" "./mbedtls/EFR32/asn1parse.o" "./mbedtls/EFR32/asn1write.o" "./mbedtls/EFR32/base64.o" "./mbedtls/EFR32/bignum.o" "./mbedtls/EFR32/blowfish.o" "./mbedtls/EFR32/camellia.o" "./mbedtls/EFR32/ccm.o" "./mbedtls/EFR32/certs.o" "./mbedtls/EFR32/cipher.o" "./mbedtls/EFR32/cipher_wrap.o" "./mbedtls/EFR32/cmac.o" "./mbedtls/EFR32/crypto_aes.o" "./mbedtls/EFR32/crypto_ble.o" "./mbedtls/EFR32/crypto_ecp.o" "./mbedtls/EFR32/crypto_management.o" "./mbedtls/EFR32/crypto_sha.o" "./mbedtls/EFR32/cryptoacc_aes.o" "./mbedtls/EFR32/cryptoacc_ccm.o" "./mbedtls/EFR32/cryptoacc_cmac.o" "./mbedtls/EFR32/cryptoacc_ecp.o" "./mbedtls/EFR32/cryptoacc_gcm.o" "./mbedtls/EFR32/cryptoacc_management.o" "./mbedtls/EFR32/cryptoacc_sha.o" "./mbedtls/EFR32/cryptoacc_trng.o" "./mbedtls/EFR32/ctr_drbg.o" "./mbedtls/EFR32/debug.o" "./mbedtls/EFR32/des.o" "./mbedtls/EFR32/dhm.o" "./mbedtls/EFR32/ecdh.o" "./mbedtls/EFR32/ecdsa.o" "./mbedtls/EFR32/ecjpake.o" "./mbedtls/EFR32/ecp.o" "./mbedtls/EFR32/ecp_curves.o" "./mbedtls/EFR32/entropy.o" "./mbedtls/EFR32/entropy_adc.o" "./mbedtls/EFR32/entropy_poll.o" "./mbedtls/EFR32/entropy_rail.o" "./mbedtls/EFR32/error.o" "./mbedtls/EFR32/gcm.o" "./mbedtls/EFR32/havege.o" "./mbedtls/EFR32/hmac_drbg.o" "./mbedtls/EFR32/md.o" "./mbedtls/EFR32/md2.o" "./mbedtls/EFR32/md4.o" "./mbedtls/EFR32/md5.o" "./mbedtls/EFR32/md_wrap.o" "./mbedtls/EFR32/memory_buffer_alloc.o" "./mbedtls/EFR32/net_sockets.o" "./mbedtls/EFR32/oid.o" "./mbedtls/EFR32/padlock.o" "./mbedtls/EFR32/pem.o" "./mbedtls/EFR32/pk.o" "./mbedtls/EFR32/pk_wrap.o" "./mbedtls/EFR32/pkcs11.o" "./mbedtls/EFR32/pkcs12.o" "./mbedtls/EFR32/pkcs5.o" "./mbedtls/EFR32/pkparse.o" "./mbedtls/EFR32/pkwrite.o" "./mbedtls/EFR32/radioaes.o" "./mbedtls/EFR32/radioaes_aes.o" "./mbedtls/EFR32/radioaes_ble.o" "./mbedtls/EFR32/ripemd160.o" "./mbedtls/EFR32/rsa.o" "./mbedtls/EFR32/rsa_internal.o" "./mbedtls/EFR32/se_aes.o" "./mbedtls/EFR32/se_ccm.o" "./mbedtls/EFR32/se_cmac.o" "./mbedtls/EFR32/se_ecp.o" "./mbedtls/EFR32/se_gcm.o" "./mbedtls/EFR32/se_jpake.o" "./mbedtls/EFR32/se_management.o" "./mbedtls/EFR32/se_sha.o" "./mbedtls/EFR32/se_trng.o" "./mbedtls/EFR32/sha1.o" "./mbedtls/EFR32/sha256.o" "./mbedtls/EFR32/sha512.o" "./mbedtls/EFR32/shax.o" "./mbedtls/EFR32/ssl_cache.o" "./mbedtls/EFR32/ssl_ciphersuites.o" "./mbedtls/EFR32/ssl_cli.o" "./mbedtls/EFR32/ssl_cookie.o" "./mbedtls/EFR32/ssl_srv.o" "./mbedtls/EFR32/ssl_ticket.o" "./mbedtls/EFR32/ssl_tls.o" "./mbedtls/EFR32/threading.o" "./mbedtls/EFR32/timing.o" "./mbedtls/EFR32/trng.o" "./mbedtls/EFR32/version.o" "./mbedtls/EFR32/version_features.o" "./mbedtls/EFR32/x509.o" "./mbedtls/EFR32/x509_create.o" "./mbedtls/EFR32/x509_crl.o" "./mbedtls/EFR32/x509_crt.o" "./mbedtls/EFR32/x509_csr.o" "./mbedtls/EFR32/x509write_crt.o" "./mbedtls/EFR32/x509write_csr.o" "./mbedtls/EFR32/xtea.o" "./network-steering/network-steering-cli.o" "./network-steering/network-steering-soc.o" "./network-steering/network-steering-v2.o" "./network-steering/network-steering.o" "./nvm3/EFR32/nvm3_default.o" "./nvm3/EFR32/nvm3_hal_flash.o" "./nvm3/nvm3_lock.o" "./reporting/reporting-cli.o" "./reporting/reporting-default-configuration.o" "./reporting/reporting.o" "./scan-dispatch/scan-dispatch.o" "./serial/EFR32/serial.o" "./serial/com.o" "./simple-main/simple-main.o" "./strong-random/strong-random-api.o" "./update-tc-link-key/update-tc-link-key-cli.o" "./update-tc-link-key/update-tc-link-key.o" "./zcl-framework-core/af-event.o" "./zcl-framework-core/af-main-common.o" "./zcl-framework-core/af-main-soc.o" "./zcl-framework-core/af-node.o" "./zcl-framework-core/af-security-common.o" "./zcl-framework-core/af-trust-center.o" "./zcl-framework-core/attribute-size.o" "./zcl-framework-core/attribute-storage.o" "./zcl-framework-core/attribute-table.o" "./zcl-framework-core/client-api.o" "./zcl-framework-core/core-cli.o" "./zcl-framework-core/crypto-state.o" "./zcl-framework-core/message.o" "./zcl-framework-core/multi-network.o" "./zcl-framework-core/network-cli.o" "./zcl-framework-core/option-cli.o" "./zcl-framework-core/plugin-cli.o" "./zcl-framework-core/print-formatter.o" "./zcl-framework-core/print.o" "./zcl-framework-core/process-cluster-message.o" "./zcl-framework-core/process-global-message.o" "./zcl-framework-core/security-cli.o" "./zcl-framework-core/service-discovery-common.o" "./zcl-framework-core/service-discovery-soc.o" "./zcl-framework-core/time-util.o" "./zcl-framework-core/util.o" "./zcl-framework-core/zcl-cli.o" "./zcl-framework-core/zdo-cli.o" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/debug-basic-library-cortexm3-gcc-efr32mg21-rail/debug-basic-library.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/zll-library-cortexm3-gcc-efr32mg21-rail/zll-library.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/source-route-library-cortexm3-gcc-efr32mg21-rail/source-route-library.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/end-device-bind-stub-library-cortexm3-gcc-efr32mg21-rail/end-device-bind-stub-library.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/sim-eeprom2-to-nvm3-upgrade-stub-library-cortexm3-gcc-efr32mg21-rail/sim-eeprom2-to-nvm3-upgrade-stub-library.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/cbke-283k1-stub-library-cortexm3-gcc-efr32mg21-rail/cbke-283k1-stub-library.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/debug-extended-stub-library-cortexm3-gcc-efr32mg21-rail/debug-extended-stub-library.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/cbke-library-dsa-verify-stub-cortexm3-gcc-efr32mg21-rail/cbke-library-dsa-verify-stub.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/radio/rail_lib/autogen/librail_release/librail_efr32xg21_gcc_release.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//platform/emdrv/nvm3/lib/libnvm3_CM33_gcc.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/cbke-stub-library-cortexm3-gcc-efr32mg21-rail/cbke-stub-library.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/hal-library-cortexm3-gcc-efr32mg21-rail/hal-library.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/packet-validate-stub-library-cortexm3-gcc-efr32mg21-rail/packet-validate-stub-library.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/security-library-link-keys-stub-cortexm3-gcc-efr32mg21-rail/security-library-link-keys-stub.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/binding-table-library-cortexm3-gcc-efr32mg21-rail/binding-table-library.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/cbke-163k1-stub-library-cortexm3-gcc-efr32mg21-rail/cbke-163k1-stub-library.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/cbke-library-dsa-sign-stub-cortexm3-gcc-efr32mg21-rail/cbke-library-dsa-sign-stub.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/gp-stub-library-cortexm3-gcc-efr32mg21-rail/gp-stub-library.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/multi-network-stub-library-cortexm3-gcc-efr32mg21-rail/multi-network-stub-library.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/zigbee-pro-stack-cortexm3-gcc-efr32mg21-rail/zigbee-pro-stack.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/cbke-library-dsa-verify-283k1-stub-cortexm3-gcc-efr32mg21-rail/cbke-library-dsa-verify-283k1-stub.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/install-code-library-cortexm3-gcc-efr32mg21-rail/install-code-library.a" "D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/v4/developer/sdks/gecko_sdk_suite/v2.7//protocol/zigbee/build/zigbee-r22-support-stub-library-cortexm3-gcc-efr32mg21-rail/zigbee-r22-support-stub-library.a" -lm -Wl,--end-group -Wl,--start-group -lgcc -lc -lnosys -Wl,--end-group
	@echo 'Finished building target: $@'
	@echo ' '

	@echo 'Building hex file: ZB_SZEDCLI_V1_0_0.hex'
	arm-none-eabi-objcopy -O ihex "ZB_SZEDCLI_V1_0_0.axf" "ZB_SZEDCLI_V1_0_0.hex"
	@echo ' '

	@echo 'Building bin file: ZB_SZEDCLI_V1_0_0.bin'
	arm-none-eabi-objcopy -O binary "ZB_SZEDCLI_V1_0_0.axf" "ZB_SZEDCLI_V1_0_0.bin"
	@echo ' '

	@echo 'Building s37 file: ZB_SZEDCLI_V1_0_0.s37'
	arm-none-eabi-objcopy -O srec "ZB_SZEDCLI_V1_0_0.axf" "ZB_SZEDCLI_V1_0_0.s37"
	@echo ' '

	@echo 'Running size tool'
	arm-none-eabi-size "ZB_SZEDCLI_V1_0_0.axf" -A
	@echo ' '

	$(MAKE) --no-print-directory post-build

# Other Targets
clean:
	-$(RM) $(EXECUTABLES)$(OBJS)$(C_DEPS) ZB_SZEDCLI_V1_0_0.axf
	-@echo ' '

pre-build:
	-cmd //c 'D:\DH\Lumi\Zigbee\SimplicityStudio\SimplicityStudio\MyWorkspace\ZB_SZEDCLI_V1_0_0/ZB_SZEDCLI_V1_0_0-prebuild.bat' 'ZB_SZEDCLI_V1_0_0' 'D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/MyWorkspace/ZB_SZEDCLI_V1_0_0' '' 'D:\DH\Lumi\Zigbee\SimplicityStudio\SimplicityStudio\v4'
	-@echo ' '

post-build:
	-cmd //c 'D:\DH\Lumi\Zigbee\SimplicityStudio\SimplicityStudio\MyWorkspace\ZB_SZEDCLI_V1_0_0/ZB_SZEDCLI_V1_0_0-postbuild.bat' 'ZB_SZEDCLI_V1_0_0' 'D:/DH/Lumi/Zigbee/SimplicityStudio/SimplicityStudio/MyWorkspace/ZB_SZEDCLI_V1_0_0' '' 'D:\DH\Lumi\Zigbee\SimplicityStudio\SimplicityStudio\v4'
	-@echo ' '

.PHONY: all clean dependents
.SECONDARY: main-build pre-build post-build

-include ../makefile.targets

# This file is generated by objective.metadata
#
# Last update: Sun Feb 20 18:46:06 2022
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
misc.update(
    {
        "ScriptCodeRun": objc.createStructType(
            "CoreServices.CarbonCore.ScriptCodeRun",
            b"{ScriptCodeRun=Qs}",
            ["offset", "script"],
        ),
        "NumFormatStringRec": objc.createStructType(
            "CoreServices.CarbonCore.NumFormatStringRec",
            b"{NumFormatString=CC[254c]}",
            ["fLength", "fVersion", "data"],
        ),
        "UnicodeMapping": objc.createStructType(
            "CoreServices.CarbonCore.UnicodeMapping",
            b"{UnicodeMapping=IIi}",
            ["unicodeEncoding", "otherEncoding", "mappingVersion"],
        ),
        "TECConversionInfo": objc.createStructType(
            "CoreServices.CarbonCore.TECConversionInfo",
            b"{TECConversionInfo=IISS}",
            ["sourceEncoding", "destinationEncoding", "reserved1", "reserved2"],
        ),
        "LocaleAndVariant": objc.createStructType(
            "CoreServices.CarbonCore.LocaleAndVariant",
            b"{LocaleAndVariant=^{OpaqueLocaleRef=}I}",
            ["locale", "opVariant"],
        ),
        "TextEncodingRun": objc.createStructType(
            "CoreServices.CarbonCore.TextEncodingRun",
            b"{TextEncodingRun=QI}",
            ["offset", "textEncoding"],
        ),
        "TECInfo": objc.createStructType(
            "CoreServices.CarbonCore.TECInfo",
            b"{TECInfo=SSIII[32C][32C]SS}",
            [
                "format",
                "tecVersion",
                "tecTextConverterFeatures",
                "tecUnicodeConverterFeatures",
                "tecTextCommonFeatures",
                "tecTextEncodingsFolderName",
                "tecExtensionFileName",
                "tecLowestTEFileVersion",
                "tecHighestTEFileVersion",
            ],
        ),
        "Nanoseconds": objc.createStructType(
            "CoreServices.CarbonCore.Nanoseconds", b"{UnsignedWide=II}", ["lo", "hi"]
        ),
    }
)
constants = """$$"""
enums = """$gestaltArm@20$kBig5_BasicVariant@0$kBig5_DOSVariant@3$kBig5_ETenVariant@2$kBig5_StandardVariant@1$kCSDiskSpaceRecoveryOptionNoUI@1$kDOSJapanesePalmVariant@1$kDOSJapaneseStandardVariant@0$kEUC_CN_BasicVariant@0$kEUC_CN_DOSVariant@1$kEUC_KR_BasicVariant@0$kEUC_KR_DOSVariant@1$kFSAllowConcurrentAsyncIOBit@3$kHebrewFigureSpaceVariant@1$kHebrewStandardVariant@0$kISOLatin1MusicCDVariant@1$kISOLatin1StandardVariant@0$kISOLatinArabicExplicitOrderVariant@2$kISOLatinArabicImplicitOrderVariant@0$kISOLatinArabicVisualOrderVariant@1$kISOLatinHebrewExplicitOrderVariant@2$kISOLatinHebrewImplicitOrderVariant@0$kISOLatinHebrewVisualOrderVariant@1$kJapaneseBasicVariant@2$kJapanesePostScriptPrintVariant@4$kJapanesePostScriptScrnVariant@3$kJapaneseStandardVariant@0$kJapaneseStdNoVerticalsVariant@1$kJapaneseVertAtKuPlusTenVariant@5$kLocaleAllPartsMask@63$kLocaleAndVariantNameMask@3$kLocaleLanguageMask@1$kLocaleLanguageVariantMask@2$kLocaleNameMask@1$kLocaleOperationVariantNameMask@2$kLocaleRegionMask@16$kLocaleRegionVariantMask@32$kLocaleScriptMask@4$kLocaleScriptVariantMask@8$kMacArabicAlBayanVariant@3$kMacArabicStandardVariant@0$kMacArabicThuluthVariant@2$kMacArabicTrueTypeVariant@1$kMacCroatianCurrencySignVariant@1$kMacCroatianDefaultVariant@0$kMacCroatianEuroSignVariant@2$kMacCyrillicCurrSignStdVariant@1$kMacCyrillicCurrSignUkrVariant@2$kMacCyrillicDefaultVariant@0$kMacCyrillicEuroSignVariant@3$kMacFarsiStandardVariant@0$kMacFarsiTrueTypeVariant@1$kMacGreekDefaultVariant@0$kMacGreekEuroSignVariant@2$kMacGreekNoEuroSignVariant@1$kMacHebrewFigureSpaceVariant@1$kMacHebrewStandardVariant@0$kMacIcelandicStandardVariant@0$kMacIcelandicStdCurrSignVariant@2$kMacIcelandicStdDefaultVariant@0$kMacIcelandicStdEuroSignVariant@4$kMacIcelandicTTCurrSignVariant@3$kMacIcelandicTTDefaultVariant@1$kMacIcelandicTTEuroSignVariant@5$kMacIcelandicTrueTypeVariant@1$kMacJapaneseBasicVariant@2$kMacJapanesePostScriptPrintVariant@4$kMacJapanesePostScriptScrnVariant@3$kMacJapaneseStandardVariant@0$kMacJapaneseStdNoVerticalsVariant@1$kMacJapaneseVertAtKuPlusTenVariant@5$kMacRomanCurrencySignVariant@1$kMacRomanDefaultVariant@0$kMacRomanEuroSignVariant@2$kMacRomanLatin1CroatianVariant@8$kMacRomanLatin1DefaultVariant@0$kMacRomanLatin1IcelandicVariant@11$kMacRomanLatin1RomanianVariant@14$kMacRomanLatin1StandardVariant@2$kMacRomanLatin1TurkishVariant@6$kMacRomanStandardVariant@0$kMacRomanianCurrencySignVariant@1$kMacRomanianDefaultVariant@0$kMacRomanianEuroSignVariant@2$kMacVT100CurrencySignVariant@1$kMacVT100DefaultVariant@0$kMacVT100EuroSignVariant@2$kShiftJIS_BasicVariant@0$kShiftJIS_DOSVariant@1$kShiftJIS_MusicCDVariant@2$kTECAddFallbackInterruptBit@7$kTECAddFallbackInterruptMask@128$kTECAddForceASCIIChangesBit@4$kTECAddForceASCIIChangesMask@16$kTECAddTextRunHeuristicsBit@6$kTECAddTextRunHeuristicsMask@64$kTECChinesePluginSignature@1887070319$kTECDisableFallbacksBit@16$kTECDisableFallbacksMask@65536$kTECDisableLooseMappingsBit@17$kTECDisableLooseMappingsMask@131072$kTECFallbackTextLengthFixBit@1$kTECFallbackTextLengthFixMask@2$kTECInfoCurrentFormat@2$kTECInternetNameDefaultUsageMask@0$kTECInternetNameStrictUsageMask@1$kTECInternetNameTolerantUsageMask@2$kTECJapanesePluginSignature@1886023790$kTECKeepInfoFixBit@0$kTECKeepInfoFixMask@1$kTECKoreanPluginSignature@1886089074$kTECPreferredEncodingFixBit@5$kTECPreferredEncodingFixMask@32$kTECSignature@1701733238$kTECTextRunBitClearFixBit@2$kTECTextRunBitClearFixMask@4$kTECTextToUnicodeScanFixBit@3$kTECTextToUnicodeScanFixMask@8$kTECUnicodePluginSignature@1886744169$kTEC_MIBEnumDontCare@-1$kTextCenter@1$kTextEncodingANSEL@1537$kTextEncodingBaseName@1$kTextEncodingBig5@2563$kTextEncodingBig5_E@2569$kTextEncodingBig5_HKSCS_1999@2566$kTextEncodingCNS_11643_92_P1@1617$kTextEncodingCNS_11643_92_P2@1618$kTextEncodingCNS_11643_92_P3@1619$kTextEncodingDOSArabic@1049$kTextEncodingDOSBalticRim@1030$kTextEncodingDOSCanadianFrench@1048$kTextEncodingDOSChineseSimplif@1057$kTextEncodingDOSChineseTrad@1059$kTextEncodingDOSCyrillic@1043$kTextEncodingDOSGreek@1029$kTextEncodingDOSGreek1@1041$kTextEncodingDOSGreek2@1052$kTextEncodingDOSHebrew@1047$kTextEncodingDOSIcelandic@1046$kTextEncodingDOSJapanese@1056$kTextEncodingDOSKorean@1058$kTextEncodingDOSLatin1@1040$kTextEncodingDOSLatin2@1042$kTextEncodingDOSLatinUS@1024$kTextEncodingDOSNordic@1050$kTextEncodingDOSPortuguese@1045$kTextEncodingDOSRussian@1051$kTextEncodingDOSThai@1053$kTextEncodingDOSTurkish@1044$kTextEncodingDefaultFormat@0$kTextEncodingDefaultVariant@0$kTextEncodingEBCDIC_CP037@3074$kTextEncodingEBCDIC_LatinCore@3073$kTextEncodingEBCDIC_US@3073$kTextEncodingEUC_CN@2352$kTextEncodingEUC_JP@2336$kTextEncodingEUC_KR@2368$kTextEncodingEUC_TW@2353$kTextEncodingFormatName@3$kTextEncodingFullName@0$kTextEncodingGBK_95@1585$kTextEncodingGB_18030_2000@1586$kTextEncodingGB_18030_2005@1586$kTextEncodingGB_2312_80@1584$kTextEncodingHZ_GB_2312@2565$kTextEncodingISO10646_1993@257$kTextEncodingISOLatin1@513$kTextEncodingISOLatin10@528$kTextEncodingISOLatin2@514$kTextEncodingISOLatin3@515$kTextEncodingISOLatin4@516$kTextEncodingISOLatin5@521$kTextEncodingISOLatin6@522$kTextEncodingISOLatin7@525$kTextEncodingISOLatin8@526$kTextEncodingISOLatin9@527$kTextEncodingISOLatinArabic@518$kTextEncodingISOLatinCyrillic@517$kTextEncodingISOLatinGreek@519$kTextEncodingISOLatinHebrew@520$kTextEncodingISO_2022_CN@2096$kTextEncodingISO_2022_CN_EXT@2097$kTextEncodingISO_2022_JP@2080$kTextEncodingISO_2022_JP_1@2082$kTextEncodingISO_2022_JP_2@2081$kTextEncodingISO_2022_JP_3@2083$kTextEncodingISO_2022_KR@2112$kTextEncodingJIS_C6226_78@1572$kTextEncodingJIS_X0201_76@1568$kTextEncodingJIS_X0208_83@1569$kTextEncodingJIS_X0208_90@1570$kTextEncodingJIS_X0212_90@1571$kTextEncodingJIS_X0213_MenKuTen@1577$kTextEncodingKOI8_R@2562$kTextEncodingKOI8_U@2568$kTextEncodingKSC_5601_87@1600$kTextEncodingKSC_5601_92_Johab@1601$kTextEncodingMacArabic@4$kTextEncodingMacArmenian@24$kTextEncodingMacBengali@13$kTextEncodingMacBurmese@19$kTextEncodingMacCeltic@39$kTextEncodingMacCentralEurRoman@29$kTextEncodingMacChineseSimp@25$kTextEncodingMacChineseTrad@2$kTextEncodingMacCroatian@36$kTextEncodingMacCyrillic@7$kTextEncodingMacDevanagari@9$kTextEncodingMacDingbats@34$kTextEncodingMacEastEurRoman@29$kTextEncodingMacEthiopic@28$kTextEncodingMacExtArabic@31$kTextEncodingMacFarsi@140$kTextEncodingMacGaelic@40$kTextEncodingMacGeez@28$kTextEncodingMacGeorgian@23$kTextEncodingMacGreek@6$kTextEncodingMacGujarati@11$kTextEncodingMacGurmukhi@10$kTextEncodingMacHFS@255$kTextEncodingMacHebrew@5$kTextEncodingMacIcelandic@37$kTextEncodingMacInuit@236$kTextEncodingMacJapanese@1$kTextEncodingMacKannada@16$kTextEncodingMacKeyboardGlyphs@41$kTextEncodingMacKhmer@20$kTextEncodingMacKorean@3$kTextEncodingMacLaotian@22$kTextEncodingMacMalayalam@17$kTextEncodingMacMongolian@27$kTextEncodingMacOriya@12$kTextEncodingMacRSymbol@8$kTextEncodingMacRoman@0$kTextEncodingMacRomanLatin1@2564$kTextEncodingMacRomanian@38$kTextEncodingMacSimpChinese@25$kTextEncodingMacSinhalese@18$kTextEncodingMacSymbol@33$kTextEncodingMacTamil@14$kTextEncodingMacTelugu@15$kTextEncodingMacThai@21$kTextEncodingMacTibetan@26$kTextEncodingMacTradChinese@2$kTextEncodingMacTurkish@35$kTextEncodingMacUkrainian@152$kTextEncodingMacUnicode@126$kTextEncodingMacUninterp@32$kTextEncodingMacVT100@252$kTextEncodingMacVietnamese@30$kTextEncodingMultiRun@4095$kTextEncodingNextStepJapanese@2818$kTextEncodingNextStepLatin@2817$kTextEncodingShiftJIS@2561$kTextEncodingShiftJIS_X0213@1576$kTextEncodingShiftJIS_X0213_00@1576$kTextEncodingUS_ASCII@1536$kTextEncodingUnicodeDefault@256$kTextEncodingUnicodeV10_0@276$kTextEncodingUnicodeV11_0@277$kTextEncodingUnicodeV12_1@278$kTextEncodingUnicodeV13_0@279$kTextEncodingUnicodeV1_1@257$kTextEncodingUnicodeV2_0@259$kTextEncodingUnicodeV2_1@259$kTextEncodingUnicodeV3_0@260$kTextEncodingUnicodeV3_1@261$kTextEncodingUnicodeV3_2@262$kTextEncodingUnicodeV4_0@264$kTextEncodingUnicodeV5_0@266$kTextEncodingUnicodeV5_1@267$kTextEncodingUnicodeV6_0@269$kTextEncodingUnicodeV6_1@270$kTextEncodingUnicodeV6_3@272$kTextEncodingUnicodeV7_0@273$kTextEncodingUnicodeV8_0@274$kTextEncodingUnicodeV9_0@275$kTextEncodingUnknown@65535$kTextEncodingVISCII@2567$kTextEncodingVariantName@2$kTextEncodingWindowsANSI@1280$kTextEncodingWindowsArabic@1286$kTextEncodingWindowsBalticRim@1287$kTextEncodingWindowsCyrillic@1282$kTextEncodingWindowsGreek@1283$kTextEncodingWindowsHebrew@1285$kTextEncodingWindowsKoreanJohab@1296$kTextEncodingWindowsLatin1@1280$kTextEncodingWindowsLatin2@1281$kTextEncodingWindowsLatin5@1284$kTextEncodingWindowsVietnamese@1288$kTextFlushDefault@0$kTextFlushLeft@-2$kTextFlushRight@-1$kTextLanguageDontCare@-128$kTextRegionDontCare@-128$kTextScriptDontCare@-128$kUCBidiCatArabicNumber@6$kUCBidiCatBlockSeparator@8$kUCBidiCatBoundaryNeutral@19$kUCBidiCatCommonNumberSeparator@7$kUCBidiCatEuroNumber@3$kUCBidiCatEuroNumberSeparator@4$kUCBidiCatEuroNumberTerminator@5$kUCBidiCatFirstStrongIsolate@22$kUCBidiCatLeftRight@1$kUCBidiCatLeftRightEmbedding@13$kUCBidiCatLeftRightIsolate@20$kUCBidiCatLeftRightOverride@15$kUCBidiCatNonSpacingMark@18$kUCBidiCatNotApplicable@0$kUCBidiCatOtherNeutral@11$kUCBidiCatPopDirectionalFormat@17$kUCBidiCatPopDirectionalIsolate@23$kUCBidiCatRightLeft@2$kUCBidiCatRightLeftArabic@12$kUCBidiCatRightLeftEmbedding@14$kUCBidiCatRightLeftIsolate@21$kUCBidiCatRightLeftOverride@16$kUCBidiCatSegmentSeparator@9$kUCBidiCatWhitespace@10$kUCCharPropTypeBidiCategory@3$kUCCharPropTypeCombiningClass@2$kUCCharPropTypeDecimalDigitValue@4$kUCCharPropTypeGenlCategory@1$kUCGenlCatLetterLowercase@15$kUCGenlCatLetterModifier@17$kUCGenlCatLetterOther@18$kUCGenlCatLetterTitlecase@16$kUCGenlCatLetterUppercase@14$kUCGenlCatMarkEnclosing@7$kUCGenlCatMarkNonSpacing@5$kUCGenlCatMarkSpacingCombining@6$kUCGenlCatNumberDecimalDigit@8$kUCGenlCatNumberLetter@9$kUCGenlCatNumberOther@10$kUCGenlCatOtherControl@1$kUCGenlCatOtherFormat@2$kUCGenlCatOtherNotAssigned@0$kUCGenlCatOtherPrivateUse@4$kUCGenlCatOtherSurrogate@3$kUCGenlCatPunctClose@23$kUCGenlCatPunctConnector@20$kUCGenlCatPunctDash@21$kUCGenlCatPunctFinalQuote@25$kUCGenlCatPunctInitialQuote@24$kUCGenlCatPunctOpen@22$kUCGenlCatPunctOther@26$kUCGenlCatSeparatorLine@12$kUCGenlCatSeparatorParagraph@13$kUCGenlCatSeparatorSpace@11$kUCGenlCatSymbolCurrency@29$kUCGenlCatSymbolMath@28$kUCGenlCatSymbolModifier@30$kUCGenlCatSymbolOther@31$kUCHighSurrogateRangeEnd@56319$kUCHighSurrogateRangeStart@55296$kUCLowSurrogateRangeEnd@57343$kUCLowSurrogateRangeStart@56320$kUnicode16BitFormat@0$kUnicode32BitFormat@3$kUnicodeByteOrderMark@65279$kUnicodeCanonicalCompVariant@3$kUnicodeCanonicalDecompVariant@2$kUnicodeFallbackInterruptSafeMask@4$kUnicodeFallbackSequencingMask@3$kUnicodeHFSPlusCompVariant@9$kUnicodeHFSPlusDecompVariant@8$kUnicodeMaxDecomposedVariant@2$kUnicodeNoCompatibilityVariant@1$kUnicodeNoComposedVariant@3$kUnicodeNoCorporateVariant@4$kUnicodeNoSubset@0$kUnicodeNormalizationFormC@3$kUnicodeNormalizationFormD@5$kUnicodeNotAChar@65535$kUnicodeObjectReplacement@65532$kUnicodeReplacementChar@65533$kUnicodeSCSUFormat@8$kUnicodeSwappedByteOrderMark@65534$kUnicodeUTF16BEFormat@4$kUnicodeUTF16Format@0$kUnicodeUTF16LEFormat@5$kUnicodeUTF32BEFormat@6$kUnicodeUTF32Format@3$kUnicodeUTF32LEFormat@7$kUnicodeUTF7Format@1$kUnicodeUTF8Format@2$kWindowsLatin1PalmVariant@1$kWindowsLatin1StandardVariant@0$"""
misc.update({})
misc.update(
    {"kTECMacOSXDispatchTableNameString": b"ConverterPluginGetPluginDispatchTable"}
)
functions = {
    "CSBackupIsItemExcluded": (
        b"Z^{__CFURL=}^Z",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "CSDiskSpaceStartRecovery": (
        b"v^{__CFURL=}Qi^^{__CFUUID=}@@?",
        "",
        {
            "arguments": {
                3: {"type_modifier": "o"},
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"type": "Z"},
                            2: {"type": "Q"},
                            3: {"type": "@"},
                        },
                    }
                },
            }
        },
    ),
    "GetTextEncodingFormat": (b"II",),
    "LocaleStringToLangAndRegionCodes": (
        b"i^t^s^s",
        "",
        {
            "arguments": {
                0: {"c_array_delimited_by_null": True, "type_modifier": "n"},
                1: {"type_modifier": "o"},
                2: {"type_modifier": "o"},
            }
        },
    ),
    "TECCreateSniffer": (
        b"i^^{OpaqueTECSnifferObjectRef=}^IQ",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                0: {"type_modifier": "o"},
                1: {"c_array_length_in_arg": 2, "type_modifier": "n"},
            },
        },
    ),
    "TECGetTextEncodingFromInternetNameOrMIB": (
        b"i^II^{__CFString=}i",
        "",
        {
            "arguments": {
                0: {"type_modifier": "o"},
            }
        },
    ),
    "GetTextEncodingFromScriptInfo": (
        b"isss^I",
        "",
        {"arguments": {3: {"type_modifier": "o"}}},
    ),
    "TECClearConverterContextInfo": (b"i^{OpaqueTECObjectRef=}",),
    "TECGetWebTextEncodings": (
        b"is^IQ^Q",
        "",
        {
            "arguments": {
                1: {"c_array_length_in_arg": (2, 3), "type_modifier": "o"},
                3: {"type_modifier": "o"},
            }
        },
    ),
    "TECCountWebTextEncodings": (
        b"is^Q",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "LocaleRefGetPartString": (
        b"i^{OpaqueLocaleRef=}IQ^t",
        "",
        {"arguments": {3: {"c_array_delimited_by_null": True, "type_modifier": "o"}}},
    ),
    "UCIsSurrogateLowCharacter": (b"ZT",),
    "TECCreateOneToManyConverter": (
        b"i^^{OpaqueTECObjectRef=}IQ^I",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                0: {"type_modifier": "o"},
                3: {"c_array_length_in_arg": 2, "type_modifier": "n"},
            },
        },
    ),
    "TECGetMailTextEncodings": (
        b"is^IQ^Q",
        "",
        {
            "arguments": {
                1: {"c_array_length_in_arg": (2, 3), "type_modifier": "o"},
                3: {"type_modifier": "o"},
            }
        },
    ),
    "TECSniffTextEncoding": (
        b"i^{OpaqueTECSnifferObjectRef=}^CQ^IQ^QQ^QQ",
        "",
        {
            "arguments": {
                1: {"c_array_length_in_arg": 2, "type_modifier": "n"},
                3: {"c_array_length_in_arg": 4, "type_modifier": "o"},
                5: {"c_array_length_in_arg": 6, "type_modifier": "o"},
                7: {"c_array_length_in_arg": 8, "type_modifier": "o"},
            }
        },
    ),
    "TECGetInfo": (
        b"i^^^{TECInfo=SSIII[32C][32C]SS}",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "CreateTextEncoding": (b"IIII", "", {"retval": {"already_cfretained": True}}),
    "TECCountDirectTextEncodingConversions": (
        b"i^Q",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "TECGetTextEncodingInternetName": (
        b"iI[256C]",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "TECCountAvailableSniffers": (
        b"i^Q",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "ResolveDefaultTextEncoding": (b"II",),
    "LocaleRefFromLocaleString": (
        b"i^t^^{OpaqueLocaleRef=}",
        "",
        {
            "arguments": {
                0: {"c_array_delimited_by_null": True, "type_modifier": "n"},
                1: {"type_modifier": "o"},
            }
        },
    ),
    "GetTextEncodingBase": (b"II",),
    "TECGetAvailableSniffers": (
        b"i^IQ^Q",
        "",
        {
            "arguments": {
                0: {"c_array_length_in_arg": (1, 2), "type_modifier": "o"},
                2: {"type_modifier": "o"},
            }
        },
    ),
    "TECSetBasicOptions": (b"i^{OpaqueTECObjectRef=}I",),
    "CSBackupSetItemExcluded": (b"i^{__CFURL=}ZZ",),
    "CSDiskSpaceGetRecoveryEstimate": (b"Q^{__CFURL=}",),
    "LocaleOperationCountNames": (b"iI^Q",),
    "TECDisposeSniffer": (b"i^{OpaqueTECSnifferObjectRef=}",),
    "TECConvertTextToMultipleEncodings": (
        b"i^{OpaqueTECObjectRef=}^CQ^Q^CQ^Q^{TextEncodingRun=QI}Q^Q",
        "",
        {
            "arguments": {
                1: {"c_array_length_in_arg": 2, "type_modifier": "n"},
                3: {"type_modifier": "o"},
                4: {"c_array_length_in_arg": (5, 6), "type_modifier": "o"},
                6: {"type_modifier": "o"},
                7: {"c_array_length_in_arg": (8, 9), "type_modifier": "o"},
                9: {"type_modifier": "o"},
            }
        },
    ),
    "TECFlushText": (
        b"i^{OpaqueTECObjectRef=}^CQ^Q",
        "",
        {
            "arguments": {
                1: {"c_array_length_in_arg": (2, 3), "type_modifier": "o"},
                3: {"type_modifier": "o"},
            }
        },
    ),
    "UpgradeScriptInfoToTextEncoding": (
        b"isss^C^I",
        "",
        {"arguments": {3: {"type_modifier": "n"}, 4: {"type_modifier": "o"}}},
    ),
    "TECClearSnifferContextInfo": (b"i^{OpaqueTECSnifferObjectRef=}",),
    "UCGetUnicodeScalarValueForSurrogatePair": (b"ITT",),
    "UCIsSurrogateHighCharacter": (b"ZT",),
    "TECCountSubTextEncodings": (
        b"iI^Q",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "TECConvertText": (
        b"i^{OpaqueTECObjectRef=}^CQ^Q^CQ^Q",
        "",
        {
            "arguments": {
                1: {"c_array_length_in_arg": 2, "type_modifier": "n"},
                3: {"type_modifier": "o"},
                4: {"c_array_length_in_arg": (5, 6), "type_modifier": "o"},
                6: {"type_modifier": "o"},
            }
        },
    ),
    "TECGetDirectTextEncodingConversions": (
        b"i^{TECConversionInfo=IISS}Q^Q",
        "",
        {
            "arguments": {
                0: {"c_array_length_in_arg": (1, 2), "type_modifier": "o"},
                2: {"type_modifier": "o"},
            }
        },
    ),
    "GetTextEncodingName": (
        b"iIIsIQ^Q^s^I^t",
        "",
        {
            "arguments": {
                8: {"c_array_length_in_arg": (4, 5), "type_modifier": "o"},
                5: {"type_modifier": "o"},
                6: {"type_modifier": "o"},
                7: {"type_modifier": "o"},
            }
        },
    ),
    "RevertTextEncodingToScriptInfo": (
        b"iI^s^s[256C]",
        "",
        {
            "arguments": {
                1: {"type_modifier": "o"},
                2: {"type_modifier": "o"},
                3: {"type_modifier": "o"},
            }
        },
    ),
    "TECGetSubTextEncodings": (
        b"iI^IQ^Q",
        "",
        {
            "arguments": {
                1: {"c_array_length_in_arg": (2, 3), "type_modifier": "o"},
                3: {"type_modifier": "o"},
            }
        },
    ),
    "TECCopyTextEncodingInternetNameAndMIB": (
        b"iII^^{__CFString=}^i",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                2: {"already_cfretained": True, "type_modifier": "o"},
                3: {"type_modifier": "o"},
            },
        },
    ),
    "TECGetAvailableTextEncodings": (
        b"i^IQ^Q",
        "",
        {
            "arguments": {
                0: {"c_array_length_in_arg": (1, 2), "type_modifier": "o"},
                2: {"type_modifier": "o"},
            }
        },
    ),
    "UCGetCharProperty": (
        b"i^TQi^I",
        "",
        {
            "arguments": {
                0: {"c_array_length_in_arg": 1, "type_modifier": "n"},
                3: {"type_modifier": "o"},
            }
        },
    ),
    "LocaleRefFromLangOrRegionCode": (
        b"iss^^{OpaqueLocaleRef=}",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "TECCreateConverterFromPath": (
        b"i^^{OpaqueTECObjectRef=}^IQ",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                0: {"type_modifier": "o"},
                1: {"c_array_length_in_arg": 2, "type_modifier": "n"},
            },
        },
    ),
    "TECCreateConverter": (
        b"i^^{OpaqueTECObjectRef=}II",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {0: {"type_modifier": "o"}},
        },
    ),
    "NearestMacTextEncodings": (
        b"iI^I^I",
        "",
        {"arguments": {1: {"type_modifier": "o"}, 2: {"type_modifier": "o"}}},
    ),
    "TECCountMailTextEncodings": (
        b"is^Q",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "TECCountAvailableTextEncodings": (
        b"i^Q",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "TECGetDestinationTextEncodings": (
        b"iI^IQ^Q",
        "",
        {
            "arguments": {
                1: {"c_array_length_in_arg": (2, 3), "type_modifier": "o"},
                3: {"type_modifier": "o"},
            }
        },
    ),
    "LocaleOperationGetName": (
        b"iI^{OpaqueLocaleRef=}Q^Q^t",
        "",
        {
            "arguments": {
                3: {"type_modifier": "o"},
                4: {"c_array_length_in_arg": (2, 3), "type_modifier": "o"},
            }
        },
    ),
    "TECFlushMultipleEncodings": (
        b"i^{OpaqueTECObjectRef=}^CQ^Q^{TextEncodingRun=QI}Q^Q",
        "",
        {
            "arguments": {
                1: {"c_array_length_in_arg": (2, 3), "type_modifier": "o"},
                3: {"type_modifier": "o"},
                4: {"c_array_length_in_arg": (5, 6), "type_modifier": "o"},
                6: {"type_modifier": "o"},
            }
        },
    ),
    "LocaleOperationGetIndName": (
        b"iIQQ^Q^t^^{OpaqueLocaleRef=}",
        "",
        {
            "arguments": {
                3: {"type_modifier": "o"},
                4: {"c_array_length_in_arg": (2, 3), "type_modifier": "o"},
                5: {"type_modifier": "o"},
            }
        },
    ),
    "TECCountDestinationTextEncodings": (
        b"iI^Q",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "GetScriptInfoFromTextEncoding": (
        b"iI^s^s",
        "",
        {"arguments": {1: {"type_modifier": "o"}, 2: {"type_modifier": "o"}}},
    ),
    "GetTextEncodingVariant": (b"II",),
    "TECDisposeConverter": (b"i^{OpaqueTECObjectRef=}",),
    "TECGetTextEncodingFromInternetName": (
        b"i^I^C",
        "",
        {"arguments": {0: {"type_modifier": "o"}, 1: {"type_modifier": "n"}}},
    ),
    "CSDiskSpaceCancelRecovery": (b"v^{__CFUUID=}",),
}
cftypes = [
    ("FSFileOperationRef", b"^{__FSFileOperation=}", None, None),
    ("FSFileSecurityRef", b"^{__FSFileSecurity=}", None, None),
]
misc.update(
    {
        "TECSnifferObjectRef": objc.createOpaquePointerType(
            "TECSnifferObjectRef", b"^{OpaqueTECSnifferObjectRef=}"
        ),
        "TECObjectRef": objc.createOpaquePointerType(
            "TECObjectRef", b"^{OpaqueTECObjectRef=}"
        ),
    }
)
expressions = {}

# END OF FILE

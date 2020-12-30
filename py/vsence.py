#!/usr/bin/env python3
import glob
import os

def changeCompileWords():

    CompileFile = glob.glob('.vscode/compileCommands*')[0]
    with open(CompileFile, 'r') as f:
        compileWords = f.read()
    preWords = '"command": "'
    postWords = '"command": "\\"\\"'
    if postWords in compileWords:
        print("{} was already changed to {}!".format(preWords, postWords))
    else:
        ModifiedWords = compileWords.replace(preWords, postWords)
        with open(CompileFile, 'w') as f:
            f.write(ModifiedWords)
        print("{} has been changed to {}".format(preWords, postWords))

def changeCpropertyWords():
    def getInserttext():
        key ='"cStandard"'
        spaces = '            ' ### 12 spaces
        preffix = cPropertyWords.split(key)[0]
        suffix = spaces + key + cPropertyWords.split(key)[1]
        wantText = preffix + textInserted + suffix
        return wantText
        

    cPropertyFile = glob.glob('.vscode/c_cpp*')[0]
    with open(cPropertyFile, 'r') as f:
        cPropertyWords = f.read()
    CurrentProjectName = os.path.abspath('./').split('/')[-1] ### get CurrentDirectory name
    DefaultProjectName = 'MyProject'
    ### change MyProject to new Name
    textInserted = TEXT().defines.replace(DefaultProjectName, CurrentProjectName).replace(
                         DefaultProjectName.upper(), CurrentProjectName.upper())
    ### combine difines text
    if not '"defines' in cPropertyWords:
        ModifiedWords = getInserttext()
        with open(cPropertyFile, 'w') as f:
            f.write(ModifiedWords)
        print("Add defines statement.")
        print("{} has been chaned to {}".format(DefaultProjectName, CurrentProjectName))
    else:
        print('{} has already difines statement'.format(cPropertyFile))

class TEXT():
    defines =('"defines": [\n'
            '                    "IS_PROGRAM=0",\n'
            '                    "UE_EDITOR=1",\n'
            '                    "ENABLE_PGO_PROFILE=0",\n'
            '                    "USE_VORBIS_FOR_STREAMING=1",\n'
            '                    "USE_XMA2_FOR_STREAMING=1",\n'
            '                    "WITH_DEV_AUTOMATION_TESTS=1",\n'
            '                    "WITH_PERF_AUTOMATION_TESTS=1",\n'
            '                    "UNICODE",\n'
            '                    "_UNICODE",\n'
            '                    "__UNREAL__",\n'
            '                    "IS_MONOLITHIC=0",\n'
            '                    "WITH_ENGINE=1",\n'
            '                    "WITH_UNREAL_DEVELOPER_TOOLS=1",\n'
            '                    "WITH_APPLICATION_CORE=1",\n'
            '                    "WITH_COREUOBJECT=1",\n'
            '                    "USE_STATS_WITHOUT_ENGINE=0",\n'
            '                    "WITH_PLUGIN_SUPPORT=0",\n'
            '                    "WITH_ACCESSIBILITY=1",\n'
            '                    "WITH_PERFCOUNTERS=1",\n'
            '                    "USE_LOGGING_IN_SHIPPING=0",\n'
            '                    "WITH_LOGGING_TO_MEMORY=0",\n'
            '                    "USE_CACHE_FREED_OS_ALLOCS=1",\n'
            '                    "USE_CHECKS_IN_SHIPPING=0",\n'
            '                    "WITH_EDITOR=1",\n'
            '                    "WITH_SERVER_CODE=1",\n'
            '                    "WITH_CEF3=1",\n'
            '                    "WITH_LIVE_CODING=1",\n'
            '                    "WITH_XGE_CONTROLLER=1",\n'
            '                    "UBT_MODULE_MANIFEST=\"UE4Editor.modules\"",\n'
            '                    "UBT_MODULE_MANIFEST_DEBUGGAME=\"UE4Editor-Win64-DebugGame.modules\"",\n'
            '                    "UBT_COMPILED_PLATFORM=Win64",\n'
            '                    "UBT_COMPILED_TARGET=Editor",\n'
            '                    "UE_APP_NAME=\"UE4Editor\"",\n'
            '                    "NDIS_MINIPORT_MAJOR_VERSION=0",\n'
            '                    "WIN32=1",\n'
            '                    "_WIN32_WINNT=0x0601",\n'
            '                    "WINVER=0x0601",\n'
            '                    "PLATFORM_WINDOWS=1",\n'
            '                    "OVERRIDE_PLATFORM_HEADER_NAME=Windows",\n'
            '                    "NDEBUG=1",\n'
            '                    "UE_BUILD_DEVELOPMENT=1",\n'
            '                    "UE_IS_ENGINE_MODULE=0",\n'
            '                    "IMPLEMENT_ENCRYPTION_KEY_REGISTRATION()=",\n'
            '                    "IMPLEMENT_SIGNING_KEY_REGISTRATION()=",\n'
            '                    "DEPRECATED_FORGAME=DEPRECATED",\n'
            '                    "UE_DEPRECATED_FORGAME=UE_DEPRECATED",\n'
            '                    "INCLUDE_CHAOS=0",\n'
            '                    "WITH_PHYSX=1",\n'
            '                    "WITH_CHAOS=0",\n'
            '                    "WITH_CHAOS_CLOTHING=0",\n'
            '                    "WITH_CHAOS_NEEDS_TO_BE_FIXED=0",\n'
            '                    "PHYSICS_INTERFACE_PHYSX=1",\n'
            '                    "WITH_APEX=1",\n'
            '                    "WITH_APEX_CLOTHING=1",\n'
            '                    "WITH_CLOTH_COLLISION_DETECTION=1",\n'
            '                    "WITH_PHYSX_COOKING=1",\n'
            '                    "WITH_NVCLOTH=1",\n'
            '                    "WITH_CUSTOM_SQ_STRUCTURE=0",\n'
            '                    "WITH_IMMEDIATE_PHYSX=0",\n'
            '                    "GPUPARTICLE_LOCAL_VF_ONLY=0",\n'
            '                    "ENGINE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "ENGINE_API=",\n'
            '                    "UE_ENABLE_ICU=1",\n'
            '                    "WITH_VS_PERF_PROFILER=0",\n'
            '                    "WITH_DIRECTXMATH=0",\n'
            '                    "WITH_MALLOC_STOMP=1",\n'
            '                    "CORE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "CORE_API=",\n'
            '                    "TRACELOG_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "TRACELOG_API=",\n'
            '                    "COREUOBJECT_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "COREUOBJECT_API=",\n'
            '                    "NETCORE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "NETCORE_API=",\n'
            '                    "APPLICATIONCORE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "APPLICATIONCORE_API=",\n'
            '                    "RHI_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "RHI_API=",\n'
            '                    "JSON_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "JSON_API=",\n'
            '                    "WITH_FREETYPE=1",\n'
            '                    "SLATECORE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "SLATECORE_API=",\n'
            '                    "INPUTCORE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "INPUTCORE_API=",\n'
            '                    "SLATE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "SLATE_API=",\n'
            '                    "WITH_UNREALPNG=1",\n'
            '                    "WITH_UNREALJPEG=1",\n'
            '                    "WITH_UNREALEXR=1",\n'
            '                    "IMAGEWRAPPER_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "IMAGEWRAPPER_API=",\n'
            '                    "MESSAGING_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "MESSAGING_API=",\n'
            '                    "MESSAGINGCOMMON_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "MESSAGINGCOMMON_API=",\n'
            '                    "RENDERCORE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "RENDERCORE_API=",\n'
            '                    "SOCKETS_PACKAGE=1",\n'
            '                    "SOCKETS_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "SOCKETS_API=",\n'
            '                    "ASSETREGISTRY_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "ASSETREGISTRY_API=",\n'
            '                    "ENGINEMESSAGES_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "ENGINEMESSAGES_API=",\n'
            '                    "ENGINESETTINGS_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "ENGINESETTINGS_API=",\n'
            '                    "SYNTHBENCHMARK_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "SYNTHBENCHMARK_API=",\n'
            '                    "RENDERER_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "RENDERER_API=",\n'
            '                    "GAMEPLAYTAGS_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "GAMEPLAYTAGS_API=",\n'
            '                    "PACKETHANDLER_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "PACKETHANDLER_API=",\n'
            '                    "RELIABILITYHANDLERCOMPONENT_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "RELIABILITYHANDLERCOMPONENT_API=",\n'
            '                    "AUDIOPLATFORMCONFIGURATION_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "AUDIOPLATFORMCONFIGURATION_API=",\n'
            '                    "MESHDESCRIPTION_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "MESHDESCRIPTION_API=",\n'
            '                    "STATICMESHDESCRIPTION_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "STATICMESHDESCRIPTION_API=",\n'
            '                    "PAKFILE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "PAKFILE_API=",\n'
            '                    "RSA_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "RSA_API=",\n'
            '                    "NETWORKREPLAYSTREAMING_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "NETWORKREPLAYSTREAMING_API=",\n'
            '                    "PHYSICSCORE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "PHYSICSCORE_API=",\n'
            '                    "COMPILE_WITHOUT_UNREAL_SUPPORT=0",\n'
            '                    "CHAOS_MEMORY_TRACKING=0",\n'
            '                    "CHAOS_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "CHAOS_API=",\n'
            '                    "CHAOS_CHECKED=0",\n'
            '                    "CHAOSCORE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "CHAOSCORE_API=",\n'
            '                    "INTEL_ISPC=1",\n'
            '                    "VORONOI_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "VORONOI_API=",\n'
            '                    "FIELDSYSTEMCORE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "FIELDSYSTEMCORE_API=",\n'
            '                    "WITH_PHYSX_RELEASE=0",\n'
            '                    "UE_PHYSX_SUFFIX=PROFILE",\n'
            '                    "UE_APEX_SUFFIX=PROFILE",\n'
            '                    "APEX_UE4=1",\n'
            '                    "APEX_STATICALLY_LINKED=0",\n'
            '                    "WITH_APEX_LEGACY=1",\n'
            '                    "SIGNALPROCESSING_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "SIGNALPROCESSING_API=",\n'
            '                    "WITH_RECAST=1",\n'
            '                    "UNREALED_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "UNREALED_API=",\n'
            '                    "BSPMODE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "BSPMODE_API=",\n'
            '                    "DIRECTORYWATCHER_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "DIRECTORYWATCHER_API=",\n'
            '                    "DOCUMENTATION_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "DOCUMENTATION_API=",\n'
            '                    "LOAD_PLUGINS_FOR_TARGET_PLATFORMS=1",\n'
            '                    "PROJECTS_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "PROJECTS_API=",\n'
            '                    "SANDBOXFILE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "SANDBOXFILE_API=",\n'
            '                    "EDITORSTYLE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "EDITORSTYLE_API=",\n'
            '                    "SOURCE_CONTROL_WITH_SLATE=1",\n'
            '                    "SOURCECONTROL_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "SOURCECONTROL_API=",\n'
            '                    "UNREALEDMESSAGES_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "UNREALEDMESSAGES_API=",\n'
            '                    "GAMEPLAYDEBUGGER_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "GAMEPLAYDEBUGGER_API=",\n'
            '                    "BLUEPRINTGRAPH_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "BLUEPRINTGRAPH_API=",\n'
            '                    "EDITORSUBSYSTEM_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "EDITORSUBSYSTEM_API=",\n'
            '                    "HTTP_PACKAGE=1",\n'
            '                    "CURL_ENABLE_DEBUG_CALLBACK=1",\n'
            '                    "CURL_ENABLE_NO_TIMEOUTS_OPTION=1",\n'
            '                    "HTTP_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "HTTP_API=",\n'
            '                    "UNREALAUDIO_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "UNREALAUDIO_API=",\n'
            '                    "FUNCTIONALTESTING_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "FUNCTIONALTESTING_API=",\n'
            '                    "AUTOMATIONCONTROLLER_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "AUTOMATIONCONTROLLER_API=",\n'
            '                    "LOCALIZATION_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "LOCALIZATION_API=",\n'
            '                    "WITH_SNDFILE_IO=1",\n'
            '                    "AUDIOEDITOR_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "AUDIOEDITOR_API=",\n'
            '                    "AUDIOMIXER_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "AUDIOMIXER_API=",\n'
            '                    "TARGETPLATFORM_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "TARGETPLATFORM_API=",\n'
            '                    "UELIBSAMPLERATE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "UELIBSAMPLERATE_API=",\n'
            '                    "LEVELEDITOR_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "LEVELEDITOR_API=",\n'
            '                    "SETTINGS_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "SETTINGS_API=",\n'
            '                    "INTROTUTORIALS_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "INTROTUTORIALS_API=",\n'
            '                    "HEADMOUNTEDDISPLAY_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "HEADMOUNTEDDISPLAY_API=",\n'
            '                    "VREDITOR_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "VREDITOR_API=",\n'
            '                    "COMMONMENUEXTENSIONS_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "COMMONMENUEXTENSIONS_API=",\n'
            '                    "LANDSCAPE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "LANDSCAPE_API=",\n'
            '                    "PROPERTYEDITOR_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "PROPERTYEDITOR_API=",\n'
            '                    "ACTORPICKERMODE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "ACTORPICKERMODE_API=",\n'
            '                    "SCENEDEPTHPICKERMODE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "SCENEDEPTHPICKERMODE_API=",\n'
            '                    "DETAILCUSTOMIZATIONS_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "DETAILCUSTOMIZATIONS_API=",\n'
            '                    "CLASSVIEWER_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "CLASSVIEWER_API=",\n'
            '                    "GRAPHEDITOR_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "GRAPHEDITOR_API=",\n'
            '                    "STRUCTVIEWER_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "STRUCTVIEWER_API=",\n'
            '                    "CONTENTBROWSER_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "CONTENTBROWSER_API=",\n'
            '                    "ENABLE_HTTP_FOR_NFS=1",\n'
            '                    "NETWORKFILESYSTEM_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "NETWORKFILESYSTEM_API=",\n'
            '                    "UMG_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "UMG_API=",\n'
            '                    "MOVIESCENE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "MOVIESCENE_API=",\n'
            '                    "TIMEMANAGEMENT_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "TIMEMANAGEMENT_API=",\n'
            '                    "MOVIESCENETRACKS_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "MOVIESCENETRACKS_API=",\n'
            '                    "ANIMATIONCORE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "ANIMATIONCORE_API=",\n'
            '                    "PROPERTYPATH_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "PROPERTYPATH_API=",\n'
            '                    "NAVIGATIONSYSTEM_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "NAVIGATIONSYSTEM_API=",\n'
            '                    "MESHDESCRIPTIONOPERATIONS_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "MESHDESCRIPTIONOPERATIONS_API=",\n'
            '                    "MESHBUILDER_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "MESHBUILDER_API=",\n'
            '                    "MATERIALSHADERQUALITYSETTINGS_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "MATERIALSHADERQUALITYSETTINGS_API=",\n'
            '                    "INTERACTIVETOOLSFRAMEWORK_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "INTERACTIVETOOLSFRAMEWORK_API=",\n'
            '                    "TOOLMENUSEDITOR_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "TOOLMENUSEDITOR_API=",\n'
            '                    "WITH_OGGVORBIS=1",\n'
            '                    "XAUDIO2_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "XAUDIO2_API=",\n'
            '                    "AUDIOMIXERXAUDIO2_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "AUDIOMIXERXAUDIO2_API=",\n'
            '                    "ASSETTAGSEDITOR_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "ASSETTAGSEDITOR_API=",\n'
            '                    "COLLECTIONMANAGER_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "COLLECTIONMANAGER_API=",\n'
            '                    "ADDCONTENTDIALOG_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "ADDCONTENTDIALOG_API=",\n'
            '                    "USE_EMBREE=1",\n'
            '                    "MESHUTILITIES_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "MESHUTILITIES_API=",\n'
            '                    "MESHMERGEUTILITIES_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "MESHMERGEUTILITIES_API=",\n'
            '                    "HIERARCHICALLODUTILITIES_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "HIERARCHICALLODUTILITIES_API=",\n'
            '                    "MESHREDUCTIONINTERFACE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "MESHREDUCTIONINTERFACE_API=",\n'
            '                    "ASSETTOOLS_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "ASSETTOOLS_API=",\n'
            '                    "KISMETCOMPILER_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "KISMETCOMPILER_API=",\n'
            '                    "GAMEPLAYTASKS_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "GAMEPLAYTASKS_API=",\n'
            '                    "WITH_GAMEPLAY_DEBUGGER=1",\n'
            '                    "AIMODULE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "AIMODULE_API=",\n'
            '                    "KISMET_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "KISMET_API=",\n'
            '                    "PHYSICSSQ_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "PHYSICSSQ_API=",\n'
            '                    "CHAOSSOLVERS_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "CHAOSSOLVERS_API=",\n'
            '                    "GEOMETRYCOLLECTIONCORE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "GEOMETRYCOLLECTIONCORE_API=",\n'
            '                    "GEOMETRYCOLLECTIONSIMULATIONCORE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "GEOMETRYCOLLECTIONSIMULATIONCORE_API=",\n'
            '                    "CLOTHINGSYSTEMRUNTIMEINTERFACE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "CLOTHINGSYSTEMRUNTIMEINTERFACE_API=",\n'
            '                    "AUDIOMIXERCORE_VTABLE=DLLIMPORT_VTABLE",\n'
            '                    "AUDIOMIXERCORE_API=",\n'
            '                    "UE_PROJECT_NAME=MyProject",\n'
            '                    "MYPROJECT_VTABLE=DLLEXPORT_VTABLE",\n'
            '                    "MYPROJECT_API="\n'
            '                    ],\n')




if __name__ == '__main__':
    changeCompileWords()
    changeCpropertyWords()
    print('vsence program ends.')


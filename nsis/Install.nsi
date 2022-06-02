; ������Ŏg�p����ꍇ�͂�����Unicode�ɂ��邱�Ƃ𐄏�
Unicode true

; �O�����C�u�����̃C���|�[�g
!include MUI2.nsh ; Modern UI���C���N���[�h����

; �C���X�g�[���[��
!define PRODUCT_NAME "FitScreenWindow"

; �C���X�g�[���[�̃o�[�W�����B
!define PRODUCT_VERSION "4.0"

; �J����
!define CREATOR_NAME "Kawaichi"

; �E�F�u�T�C�g��URL
!define URL_WEBSITE "https://kawaichi0228.github.io/FitScreenWindow/"

; �K�v�Ȏ��s�����iuser/admin�j
RequestExecutionLevel admin

; �r���h�t�@�C���̃f�B���N�g��
!define BUILD_DIR "build"

; �t�@�r�R���̃p�X
!define PATH_FAVICON "${BUILD_DIR}\app\images\favicon.ico"

; �C���X�g�[���[�̃A�C�R��
!define MUI_ICON "${PATH_FAVICON}"

; �A���C���X�g�[���[�̃A�C�R��
!define MUI_UNICON "${PATH_FAVICON}"

; �ŏ��̉�ʂƍŌ�̉�ʂɕ\�������摜(�E�F���J���y�[�W, �t�B�j�b�V���y�[�W)
!define PATH_WELCOMEFINISHPAGE_BITMAP "nsis_welcomefinish.bmp"
!define MUI_WELCOMEFINISHPAGE_BITMAP ${PATH_WELCOMEFINISHPAGE_BITMAP}
!define MUI_UNWELCOMEFINISHPAGE_BITMAP ${PATH_WELCOMEFINISHPAGE_BITMAP} ; �A���C���X�g�[���y�[�W

; �u���C�Z���X�_�񏑈ȍ~�v�̉�ʂɕ\�������w�b�_
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_RIGHT ; �w�b�_���E�ɕ\��
!define PATH_HEADERIMAGE_BITMAP "nsis_header.bmp"
!define MUI_HEADERIMAGE_BITMAP ${PATH_HEADERIMAGE_BITMAP}
!define MUI_HEADERIMAGE_UNBITMAP ${PATH_HEADERIMAGE_BITMAP} ; �A���C���X�g�[���y�[�W

; ���k�ݒ�B�ʏ��/solid lzma���ł����k��������
SetCompressor /solid lzma

; �C���X�g�[�����̐i����ʂŎ��s���Ă��鏈���̃��b�Z�[�W��\������i�����𓀂������Ȃǁj
ShowInstDetails show

; �A���C���X�g�[�����̐i����ʂŎ��s���Ă��鏈���̃��b�Z�[�W��\������i�����폜�������Ȃǁj
ShowUnInstDetails show

; �A�v���P�[�V������
Name "${PRODUCT_NAME} v${PRODUCT_VERSION}"

; �쐬����C���X�g�[���[���ƃA���C���X�g�[���[��
!define INSTALLER_NAME "${PRODUCT_NAME}-v${PRODUCT_VERSION}-Installer.exe"
!define UNINSTALLER_NAME "Uninstall.exe"

; �C���X�g�[���[���o��
OutFile "${INSTALLER_NAME}"

; �C���X�g�[����̃f�B���N�g��
InstallDir "$PROGRAMFILES64\${PRODUCT_NAME}"

; �C���X�g�[���[�y�[�W�̍쐬
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE license-japanese.txt
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

; �A���C���X�g�[�� �y�[�W�̍쐬
!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

; ���{��UI
!insertmacro MUI_LANGUAGE "Japanese"

; ���[�U�[���C���X�g�[���[���I���������Ƃ��ɁA�x���̃��b�Z�[�W�{�b�N�X��\��
!define MUI_ABORTWARNING

; �Z�N�V����
Section
  ; �C���X�g�[���[�ɑg�ݍ��ރt�@�C���Q
  SetOutPath "$INSTDIR" ; �o�͐���w��
  File "${BUILD_DIR}\${PRODUCT_NAME}.exe"

  SetOutPath "$INSTDIR\app\src"
  File "${BUILD_DIR}\app\src\config.json"

  SetOutPath "$INSTDIR\app\images"
  File "${BUILD_DIR}\app\images\favicon.ico"

  ; �A���C���X�g�[�����o��
  WriteUninstaller "$INSTDIR\${UNINSTALLER_NAME}"
  ; �X�^�[�g ���j���[�ɃV���[�g�J�b�g��o�^
  CreateDirectory "$SMPROGRAMS\FitScreenWindow"
  SetOutPath "$INSTDIR"
  ; �f�X�N�g�b�v�ɃV���[�g�J�b�g���쐬
  CreateShortcut "$SMPROGRAMS\${PRODUCT_NAME}\${PRODUCT_NAME}.lnk" "$INSTDIR\${PRODUCT_NAME}.exe" ""
  CreateShortcut "$DESKTOP\${PRODUCT_NAME}.lnk" "$INSTDIR\${PRODUCT_NAME}.exe" ""
  ; ���W�X�g���ɓo�^
  !define RegistryKey "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
  WriteRegStr HKLM ${RegistryKey} "UninstallString" "$INSTDIR\${UNINSTALLER_NAME}"
  WriteRegStr HKLM ${RegistryKey} "DisplayIcon" "$\"$INSTDIR\app\images\favicon.ico$\""
  WriteRegStr HKLM ${RegistryKey} "DisplayName" "${PRODUCT_NAME}"
  WriteRegStr HKLM ${RegistryKey} "Publisher" "${CREATOR_NAME}"
  
  WriteRegStr HKLM ${RegistryKey} "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr HKLM ${RegistryKey} "HelpLink" "${URL_WEBSITE}"
  WriteRegStr HKLM ${RegistryKey} "URLInfoAbout" "${URL_WEBSITE}"
  WriteRegStr HKLM ${RegistryKey} "URLUpdateInfo" "${URL_WEBSITE}"
  
SectionEnd

; �A���C���X�g�[��
Section "Uninstall"
  ; �A���C���X�g�[�����폜
  Delete "$INSTDIR\${UNINSTALLER_NAME}"
  ; �t�@�C�����폜
  Delete "$INSTDIR\${PRODUCT_NAME}.exe"
  ; �f�B���N�g�����폜
  RMDir /r "$INSTDIR"
  ; �X�^�[�g ���j���[����폜
  Delete "$SMPROGRAMS\${PRODUCT_NAME}\${PRODUCT_NAME}.lnk"
  Delete "$DESKTOP\FitScreenWindow.lnk"
  RMDir "$SMPROGRAMS\FitScreenWindow"
  ; ���W�X�g�� �L�[���폜
  DeleteRegKey HKLM ${RegistryKey}
SectionEnd
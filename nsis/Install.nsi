; MEMO: MUI_xxx: NSIS�̗\���BModernUI�̗��B�u!define MUI_xxx�v�Œ�`�ł���B����ȊO��!define�̓��[�U��`�ϐ��ƂȂ�B

; -------------------------------------------------------------------------
; ��{�ݒ�
; -------------------------------------------------------------------------
; ������Ŏg�p����ꍇ�͂�����Unicode�ɂ��邱�Ƃ𐄏�
Unicode true
; �O�����C�u�����̃C���|�[�g
!include MUI2.nsh ; Modern UI���C���N���[�h����
; ���[�U�[���C���X�g�[���[���I���������Ƃ��ɁA�x���̃��b�Z�[�W�{�b�N�X��\��
!define MUI_ABORTWARNING
; �����ݒ� [user/admin]
RequestExecutionLevel admin
; ���k�ݒ�(/solid lzma: �ō����k��)
SetCompressor /solid lzma

; -------------------------------------------------------------------------
; �e�A�v�����̕ϐ���`
; -------------------------------------------------------------------------
; �C���X�g�[���[��
!define PRODUCT_NAME "FitScreenWindow"
; �C���X�g�[���[�̃o�[�W����
!define PRODUCT_VERSION "4.1"
; �J����
!define CREATOR_NAME "Kawaichi"
; �E�F�u�T�C�g��URL
!define URL_WEBSITE "https://fitscreenwindow.com/"

; -------------------------------------------------------------------------
; �e�摜�ݒ�
; -------------------------------------------------------------------------
; �t�@�r�R���̃p�X
!define PATH_FAVICON "nsis_favicon.ico"
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

; -------------------------------------------------------------------------
; [��{�ݒ�]�C���X�g�[���E�A���C���X�g�[��
; -------------------------------------------------------------------------
; �C���X�g�[�����̐i����ʂŎ��s���Ă��鏈���̃��b�Z�[�W��\������i�����𓀂������Ȃǁj
ShowInstDetails show
; �A���C���X�g�[�����̐i����ʂŎ��s���Ă��鏈���̃��b�Z�[�W��\������i�����폜�������Ȃǁj
ShowUnInstDetails show
; �A�v���P�[�V������
Name "${PRODUCT_NAME} v${PRODUCT_VERSION}"
; �쐬����C���X�g�[���[���ƃA���C���X�g�[���[�����`
!define INSTALLER_NAME "${PRODUCT_NAME}-v${PRODUCT_VERSION}-Installer.exe"
!define UNINSTALLER_NAME "Uninstall.exe"
; �C���X�g�[���[���o��
OutFile "${INSTALLER_NAME}"
; �C���X�g�[����̃f�B���N�g��
InstallDir "$PROGRAMFILES64\${PRODUCT_NAME}"

; -------------------------------------------------------------------------
; [�y�[�W�̍쐬]�C���X�g�[���E�A���C���X�g�[��
; -------------------------------------------------------------------------
; �C���X�g�[���[�y�[�W�̍쐬
!insertmacro MUI_PAGE_WELCOME
!define PATH_LICENSE_JP "license-japanese.txt"
!insertmacro MUI_PAGE_LICENSE "${PATH_LICENSE_JP}"
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

; -------------------------------------------------------------------------
; �C���X�g�[���Z�N�V����(�f�t�H���g�Z�N�V����)
; -------------------------------------------------------------------------
Section
  ; �C���X�g�[���[�ɑg�ݍ��ރt�@�C���̏o�͐�p�X �� �g�ݍ��ޓ��̓t�@�C���p�X ���`
  !define SMPROGRAMS_ALLUSER "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
  !define BUILD_DIR "build" ; �r���h�t�@�C���̃f�B���N�g��

  SetOutPath "$INSTDIR" ; INSTDIR: ���[�U����ʂŎw�肵���C���X�g�[����f�B���N�g��
  File "nsis_favicon.ico"
  File "${BUILD_DIR}\${PRODUCT_NAME}.exe"
  File "${BUILD_DIR}\app\images\favicon.ico"

  SetOutPath "$AppData\${PRODUCT_NAME}" ; $AppData: "C:\Users\<UserName>\AppData\Roaming"
  File "${BUILD_DIR}\app\src\config.json"
  
  ; �A���C���X�g�[�����o��
  WriteUninstaller "$INSTDIR\${UNINSTALLER_NAME}" ; $INSTDIR: ���[�U���C���X�g�[���[��ʂŐݒ肵���C���X�g�[����

  ; �X�^�[�g ���j���[�ɃV���[�g�J�b�g��o�^���邽�߁A�f�B���N�g�����쐬
  CreateDirectory "${SMPROGRAMS_ALLUSER}\${PRODUCT_NAME}"
  ;!define STARTMENU_USER $SMPROGRAMS ; C:\Users\<USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
  ;CreateDirectory "$SMPROGRAMS\${PRODUCT_NAME}"
  
  ; �X�^�[�g���j���[�ƃf�X�N�g�b�v�ɃV���[�g�J�b�g���쐬
  SetOutPath "$INSTDIR"
  CreateShortcut "${SMPROGRAMS_ALLUSER}\${PRODUCT_NAME}\${PRODUCT_NAME}.lnk" "$INSTDIR\${PRODUCT_NAME}.exe" ""
  ;CreateShortcut "$SMPROGRAMS\${PRODUCT_NAME}\${PRODUCT_NAME}.lnk" "$INSTDIR\${PRODUCT_NAME}.exe" ""
  CreateShortcut "$DESKTOP\${PRODUCT_NAME}.lnk" "$INSTDIR\${PRODUCT_NAME}.exe" ""

  ; �u�A���C���X�g�[���ƕύX�v�ɕ\�������e�����`(�A���C���X�g�[���̃��W�X�g���ɓo�^)
  !define RegistryKey "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
  WriteRegStr HKLM ${RegistryKey} "UninstallString" "$INSTDIR\${UNINSTALLER_NAME}"
  WriteRegStr HKLM ${RegistryKey} "DisplayIcon" "$\"$INSTDIR\nsis_favicon.ico$\"" ; �A�C�R��
  WriteRegStr HKLM ${RegistryKey} "DisplayName" "${PRODUCT_NAME}" ; �A�v���P�[�V������
  WriteRegStr HKLM ${RegistryKey} "Publisher" "${CREATOR_NAME}" ; ���s��
  WriteRegStr HKLM ${RegistryKey} "DisplayVersion" "${PRODUCT_VERSION}" ; ���i�o�[�W����
  WriteRegStr HKLM ${RegistryKey} "HelpLink" "${URL_WEBSITE}" ; �w���v�̃����N
  WriteRegStr HKLM ${RegistryKey} "URLInfoAbout" "${URL_WEBSITE}" ; �T�|�[�g�̃����N
  WriteRegStr HKLM ${RegistryKey} "URLUpdateInfo" "${URL_WEBSITE}" ; �X�V���
SectionEnd

; -------------------------------------------------------------------------
; �A���C���X�g�[���Z�N�V����
; -------------------------------------------------------------------------
Section "Uninstall"
  ; �t�@�C���ƃf�B���N�g�����폜
  Delete "$INSTDIR\${PRODUCT_NAME}.exe"
  Delete "$INSTDIR\nsis_favicon.ico"
  Delete "$INSTDIR\favicon.ico"
  Delete "$INSTDIR\${UNINSTALLER_NAME}"
  RMDir /r "$INSTDIR"
  
  Delete "$AppData\${PRODUCT_NAME}\config.json"
  RMDir /r "$AppData\${PRODUCT_NAME}"

  ; �X�^�[�g ���j���[����V���[�g�J�b�g�ƃf�B���N�g�����폜
  Delete "${SMPROGRAMS_ALLUSER}\${PRODUCT_NAME}\${PRODUCT_NAME}.lnk"
  RMDir "${SMPROGRAMS_ALLUSER}\${PRODUCT_NAME}"

  ; �f�X�N�g�b�v����V���[�g�J�b�g���폜
  Delete "$DESKTOP\${PRODUCT_NAME}.lnk"

  ; ���W�X�g�� �L�[���폜
  DeleteRegKey HKLM ${RegistryKey}
SectionEnd
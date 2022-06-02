; 多言語で使用する場合はここをUnicodeにすることを推奨
Unicode true

; 外部ライブラリのインポート
!include MUI2.nsh ; Modern UIをインクルードする

; インストーラー名
!define PRODUCT_NAME "FitScreenWindow"

; インストーラーのバージョン。
!define PRODUCT_VERSION "4.0"

; 開発者
!define CREATOR_NAME "Kawaichi"

; ウェブサイトのURL
!define URL_WEBSITE "https://kawaichi0228.github.io/FitScreenWindow/"

; 必要な実行権限（user/admin）
RequestExecutionLevel admin

; ビルドファイルのディレクトリ
!define BUILD_DIR "build"

; ファビコンのパス
!define PATH_FAVICON "${BUILD_DIR}\app\images\favicon.ico"

; インストーラーのアイコン
!define MUI_ICON "${PATH_FAVICON}"

; アンインストーラーのアイコン
!define MUI_UNICON "${PATH_FAVICON}"

; 最初の画面と最後の画面に表示される画像(ウェルカムページ, フィニッシュページ)
!define PATH_WELCOMEFINISHPAGE_BITMAP "nsis_welcomefinish.bmp"
!define MUI_WELCOMEFINISHPAGE_BITMAP ${PATH_WELCOMEFINISHPAGE_BITMAP}
!define MUI_UNWELCOMEFINISHPAGE_BITMAP ${PATH_WELCOMEFINISHPAGE_BITMAP} ; アンインストールページ

; 「ライセンス契約書以降」の画面に表示されるヘッダ
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_RIGHT ; ヘッダを右に表示
!define PATH_HEADERIMAGE_BITMAP "nsis_header.bmp"
!define MUI_HEADERIMAGE_BITMAP ${PATH_HEADERIMAGE_BITMAP}
!define MUI_HEADERIMAGE_UNBITMAP ${PATH_HEADERIMAGE_BITMAP} ; アンインストールページ

; 圧縮設定。通常は/solid lzmaが最も圧縮率が高い
SetCompressor /solid lzma

; インストール時の進捗画面で実行している処理のメッセージを表示する（何を解凍したかなど）
ShowInstDetails show

; アンインストール時の進捗画面で実行している処理のメッセージを表示する（何を削除したかなど）
ShowUnInstDetails show

; アプリケーション名
Name "${PRODUCT_NAME} v${PRODUCT_VERSION}"

; 作成するインストーラー名とアンインストーラー名
!define INSTALLER_NAME "${PRODUCT_NAME}-v${PRODUCT_VERSION}-Installer.exe"
!define UNINSTALLER_NAME "Uninstall.exe"

; インストーラーを出力
OutFile "${INSTALLER_NAME}"

; インストール先のディレクトリ
InstallDir "$PROGRAMFILES64\${PRODUCT_NAME}"

; インストーラーページの作成
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE license-japanese.txt
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

; アンインストーラ ページの作成
!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

; 日本語UI
!insertmacro MUI_LANGUAGE "Japanese"

; ユーザーがインストーラーを終了したいときに、警告のメッセージボックスを表示
!define MUI_ABORTWARNING

; セクション
Section
  ; インストーラーに組み込むファイル群
  SetOutPath "$INSTDIR" ; 出力先を指定
  File "${BUILD_DIR}\${PRODUCT_NAME}.exe"

  SetOutPath "$INSTDIR\app\src"
  File "${BUILD_DIR}\app\src\config.json"

  SetOutPath "$INSTDIR\app\images"
  File "${BUILD_DIR}\app\images\favicon.ico"

  ; アンインストーラを出力
  WriteUninstaller "$INSTDIR\${UNINSTALLER_NAME}"
  ; スタート メニューにショートカットを登録
  CreateDirectory "$SMPROGRAMS\FitScreenWindow"
  SetOutPath "$INSTDIR"
  ; デスクトップにショートカットを作成
  CreateShortcut "$SMPROGRAMS\${PRODUCT_NAME}\${PRODUCT_NAME}.lnk" "$INSTDIR\${PRODUCT_NAME}.exe" ""
  CreateShortcut "$DESKTOP\${PRODUCT_NAME}.lnk" "$INSTDIR\${PRODUCT_NAME}.exe" ""
  ; レジストリに登録
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

; アンインストーラ
Section "Uninstall"
  ; アンインストーラを削除
  Delete "$INSTDIR\${UNINSTALLER_NAME}"
  ; ファイルを削除
  Delete "$INSTDIR\${PRODUCT_NAME}.exe"
  ; ディレクトリを削除
  RMDir /r "$INSTDIR"
  ; スタート メニューから削除
  Delete "$SMPROGRAMS\${PRODUCT_NAME}\${PRODUCT_NAME}.lnk"
  Delete "$DESKTOP\FitScreenWindow.lnk"
  RMDir "$SMPROGRAMS\FitScreenWindow"
  ; レジストリ キーを削除
  DeleteRegKey HKLM ${RegistryKey}
SectionEnd
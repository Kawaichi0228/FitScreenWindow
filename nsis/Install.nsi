; MEMO: MUI_xxx: NSISの予約語。ModernUIの略。「!define MUI_xxx」で定義できる。それ以外の!defineはユーザ定義変数となる。

; -------------------------------------------------------------------------
; 基本設定
; -------------------------------------------------------------------------
; 多言語で使用する場合はここをUnicodeにすることを推奨
Unicode true
; 外部ライブラリのインポート
!include MUI2.nsh ; Modern UIをインクルードする
; ユーザーがインストーラーを終了したいときに、警告のメッセージボックスを表示
!define MUI_ABORTWARNING
; 権限設定 [user/admin]
RequestExecutionLevel admin
; 圧縮設定(/solid lzma: 最高圧縮率)
SetCompressor /solid lzma

; -------------------------------------------------------------------------
; 各アプリ情報の変数定義
; -------------------------------------------------------------------------
; インストーラー名
!define PRODUCT_NAME "FitScreenWindow"
; インストーラーのバージョン
!define PRODUCT_VERSION "4.1"
; 開発者
!define CREATOR_NAME "Kawaichi"
; ウェブサイトのURL
!define URL_WEBSITE "https://fitscreenwindow.com/"

; -------------------------------------------------------------------------
; 各画像設定
; -------------------------------------------------------------------------
; ファビコンのパス
!define PATH_FAVICON "nsis_favicon.ico"
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

; -------------------------------------------------------------------------
; [基本設定]インストール・アンインストール
; -------------------------------------------------------------------------
; インストール時の進捗画面で実行している処理のメッセージを表示する（何を解凍したかなど）
ShowInstDetails show
; アンインストール時の進捗画面で実行している処理のメッセージを表示する（何を削除したかなど）
ShowUnInstDetails show
; アプリケーション名
Name "${PRODUCT_NAME} v${PRODUCT_VERSION}"
; 作成するインストーラー名とアンインストーラー名を定義
!define INSTALLER_NAME "${PRODUCT_NAME}-v${PRODUCT_VERSION}-Installer.exe"
!define UNINSTALLER_NAME "Uninstall.exe"
; インストーラーを出力
OutFile "${INSTALLER_NAME}"
; インストール先のディレクトリ
InstallDir "$PROGRAMFILES64\${PRODUCT_NAME}"

; -------------------------------------------------------------------------
; [ページの作成]インストール・アンインストール
; -------------------------------------------------------------------------
; インストーラーページの作成
!insertmacro MUI_PAGE_WELCOME
!define PATH_LICENSE_JP "license-japanese.txt"
!insertmacro MUI_PAGE_LICENSE "${PATH_LICENSE_JP}"
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

; -------------------------------------------------------------------------
; インストールセクション(デフォルトセクション)
; -------------------------------------------------------------------------
Section
  ; インストーラーに組み込むファイルの出力先パス → 組み込む入力ファイルパス を定義
  !define SMPROGRAMS_ALLUSER "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
  !define BUILD_DIR "build" ; ビルドファイルのディレクトリ

  SetOutPath "$INSTDIR" ; INSTDIR: ユーザが画面で指定したインストール先ディレクトリ
  File "nsis_favicon.ico"
  File "${BUILD_DIR}\${PRODUCT_NAME}.exe"
  File "${BUILD_DIR}\app\images\favicon.ico"

  SetOutPath "$AppData\${PRODUCT_NAME}" ; $AppData: "C:\Users\<UserName>\AppData\Roaming"
  File "${BUILD_DIR}\app\src\config.json"
  
  ; アンインストーラを出力
  WriteUninstaller "$INSTDIR\${UNINSTALLER_NAME}" ; $INSTDIR: ユーザがインストーラー画面で設定したインストール先

  ; スタート メニューにショートカットを登録するため、ディレクトリを作成
  CreateDirectory "${SMPROGRAMS_ALLUSER}\${PRODUCT_NAME}"
  ;!define STARTMENU_USER $SMPROGRAMS ; C:\Users\<USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
  ;CreateDirectory "$SMPROGRAMS\${PRODUCT_NAME}"
  
  ; スタートメニューとデスクトップにショートカットを作成
  SetOutPath "$INSTDIR"
  CreateShortcut "${SMPROGRAMS_ALLUSER}\${PRODUCT_NAME}\${PRODUCT_NAME}.lnk" "$INSTDIR\${PRODUCT_NAME}.exe" ""
  ;CreateShortcut "$SMPROGRAMS\${PRODUCT_NAME}\${PRODUCT_NAME}.lnk" "$INSTDIR\${PRODUCT_NAME}.exe" ""
  CreateShortcut "$DESKTOP\${PRODUCT_NAME}.lnk" "$INSTDIR\${PRODUCT_NAME}.exe" ""

  ; 「アンインストールと変更」に表示される各情報を定義(アンインストールのレジストリに登録)
  !define RegistryKey "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
  WriteRegStr HKLM ${RegistryKey} "UninstallString" "$INSTDIR\${UNINSTALLER_NAME}"
  WriteRegStr HKLM ${RegistryKey} "DisplayIcon" "$\"$INSTDIR\nsis_favicon.ico$\"" ; アイコン
  WriteRegStr HKLM ${RegistryKey} "DisplayName" "${PRODUCT_NAME}" ; アプリケーション名
  WriteRegStr HKLM ${RegistryKey} "Publisher" "${CREATOR_NAME}" ; 発行元
  WriteRegStr HKLM ${RegistryKey} "DisplayVersion" "${PRODUCT_VERSION}" ; 製品バージョン
  WriteRegStr HKLM ${RegistryKey} "HelpLink" "${URL_WEBSITE}" ; ヘルプのリンク
  WriteRegStr HKLM ${RegistryKey} "URLInfoAbout" "${URL_WEBSITE}" ; サポートのリンク
  WriteRegStr HKLM ${RegistryKey} "URLUpdateInfo" "${URL_WEBSITE}" ; 更新情報
SectionEnd

; -------------------------------------------------------------------------
; アンインストールセクション
; -------------------------------------------------------------------------
Section "Uninstall"
  ; ファイルとディレクトリを削除
  Delete "$INSTDIR\${PRODUCT_NAME}.exe"
  Delete "$INSTDIR\nsis_favicon.ico"
  Delete "$INSTDIR\favicon.ico"
  Delete "$INSTDIR\${UNINSTALLER_NAME}"
  RMDir /r "$INSTDIR"
  
  Delete "$AppData\${PRODUCT_NAME}\config.json"
  RMDir /r "$AppData\${PRODUCT_NAME}"

  ; スタート メニューからショートカットとディレクトリを削除
  Delete "${SMPROGRAMS_ALLUSER}\${PRODUCT_NAME}\${PRODUCT_NAME}.lnk"
  RMDir "${SMPROGRAMS_ALLUSER}\${PRODUCT_NAME}"

  ; デスクトップからショートカットを削除
  Delete "$DESKTOP\${PRODUCT_NAME}.lnk"

  ; レジストリ キーを削除
  DeleteRegKey HKLM ${RegistryKey}
SectionEnd
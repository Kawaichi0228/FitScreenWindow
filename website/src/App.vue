<template>
  <div id="app">
    <ToggleVisbleAtScrollEvent
      startPostionToVisible="100" startPostionToHidden="90">
      <template #fadein-slot>
          <ScrollTopButton></ScrollTopButton>
      </template>
    </ToggleVisbleAtScrollEvent>

    <MainVisual></MainVisual>
    <Demonstration id="Demonstration"></Demonstration>
    <ReleaseNote id="ReleaseNote"></ReleaseNote>
    <FooterTop id="footer-top"></FooterTop>
    <FooterBottom></FooterBottom>
  </div>
</template>

<script>
// -------------------------------------------------------------------------
// Pages
// -------------------------------------------------------------------------
import MainVisual from './pages/MainVisual.vue';
import Demonstration from './pages/Demonstration.vue';
import ReleaseNote from './pages/ReleaseNote.vue';
import FooterTop from './pages/FooterTop.vue';
import FooterBottom from './pages/FooterBottom.vue';

// -------------------------------------------------------------------------
// Components
// -------------------------------------------------------------------------
import ScrollTopButton from './components/ScrollTopButton.vue';
import ToggleVisbleAtScrollEvent from "./components/ToggleVisbleAtScrollEvent.vue";

export default {
  name: "App",
  components: {
    // -------------------------------------------------------------------------
    // Pages
    // -------------------------------------------------------------------------
    MainVisual,
    Demonstration,
    ReleaseNote,
    FooterTop,
    FooterBottom,

    // -------------------------------------------------------------------------
    // Components
    // -------------------------------------------------------------------------
    ScrollTopButton,
    ToggleVisbleAtScrollEvent,
  },
};
</script>

<style lang="scss">
/*MEMO:App.vueのstyleで、appブロックに対して全体のフォントを指定*/
@import "styles/_mixin.scss";
// Webフォントのインポート
// *** Google Fonts *** https://fonts.google.com/
//@import url("https://fonts.googleapis.com/css?family=Quicksand");
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP&display=swap');
// *** awesome icon ***
@import url("https://use.fontawesome.com/releases/v5.6.4/css/all.css");

#app {
  //font-family: "Quicksand", sans-serif;
  font-family: "Noto Sans JP", sans-serif;
  text-align: center;
}

/* -------------------------------------------------------- */
/* theme setting */
/* -------------------------------------------------------- */

/* グローバルCSS変数 */
:root {
  /* セクション */
  --section-height: 600px;
  --section-padding: 50px;
  
  /* メディアクエリ */
  --pc-font-size-lv1: 26pt;
  --pc-font-size-lv2: 14pt;

  --tab-font-size-lv1: 18pt;
  --tab-font-size-lv2: 12pt;

  --sp-font-size-lv1: 18pt;
  --sp-font-size-lv2: 12pt;

  /* テーマカラー */
  --theme-color-white: #FCFCFC;
  --theme-color-black: #000;

  --theme-color-blackgray: #2C2C2C;
  --theme-color-lightred: #FF5F5F;
  --theme-color-lightblue: #83FFE6;

  --theme-color-whitelightgray: #EEE;
  --theme-color-lightgray: #CCC;
  --theme-color-gray: #666;

  /* フェードインが完了するまでの時間 */
  --fadein-time: 0.5s;
}

body {
  margin: 0; // ヘッダの余白を消す
  color: var(--theme-color-gray);
}

a {
  // aタグ初期値防止(初期値でブルーandパープル化等してしまうため)
  color: var(--theme-color-gray);
  &:visited {color: var(--theme-color-gray);} 
  display: inline-flex;
  text-decoration: none; // リンクの下線なくす
}

ul {
  list-style-type: none; // liタグの初期の「点」を消す
  padding-left: 0px; // 行頭の空白を消す
}

#header-title {
  margin-top: 0; /* ヘッダの余白を消す */
}

/* 各ページのh1タグ用 */
#content-title {
  font-size: var(--pc-font-size-lv1);
}

/* -------------------------------------------------------- */
/* -------------------------------------------------------- */
/* -------------------------------------------------------- */
</style>

<template>
  <div id="app">
    <link rel="stylesheet" href="styles/base/_variables.scss">

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
// -------------------------------------------------------------
// Pages
// -------------------------------------------------------------
import MainVisual from './pages/MainVisual.vue';
import Demonstration from './pages/Demonstration.vue';
import ReleaseNote from './pages/ReleaseNote.vue';
import FooterTop from './pages/FooterTop.vue';
import FooterBottom from './pages/FooterBottom.vue';

// -------------------------------------------------------------
// Components
// -------------------------------------------------------------
import ScrollTopButton from './components/ScrollTopButton.vue';
import ToggleVisbleAtScrollEvent from "./components/ToggleVisbleAtScrollEvent.vue";

export default {
  name: "App",
  components: {
    // -------------------------------------------------------------
    // Pages
    // -------------------------------------------------------------
    MainVisual,
    Demonstration,
    ReleaseNote,
    FooterTop,
    FooterBottom,

    // -------------------------------------------------------------
    // Components
    // -------------------------------------------------------------
    ScrollTopButton,
    ToggleVisbleAtScrollEvent,
  },
};
</script>

<style lang="scss">
// -------------------------------------------------------------
// .scssファイルのインポート
// -------------------------------------------------------------
// MEMO: 記述順が重要。上から順に読み込まる。
// グローバル変数・関数のscssを先に読み込ませることで、
// それ以降のscss内で使用できるようになる

// function
@import "styles/function/_rem.scss";

// base
@import "styles/base/_variables.scss";
@import "styles/base/_mixin.scss";
@import "styles/base/_normalize.scss";
@import "styles/base/_html_element.scss";

</style>
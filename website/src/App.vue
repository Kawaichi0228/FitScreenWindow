<template>
  <div id="app">
    <link rel="stylesheet" href="styles/base/_variables.scss">

    <ToggleVisbleAtScrollEvent
      startPostionToVisible="90" startPostionToHidden="100">
      <template #fadein-slot>
          <ScrollTopButton></ScrollTopButton>
      </template>
    </ToggleVisbleAtScrollEvent>

    <MainVisual></MainVisual>
    <Demonstration id="Demonstration"></Demonstration>
    <ReleaseNote id="ReleaseNote"></ReleaseNote>
    <FooterPj></FooterPj> <!--MEMO: 「Footer.vue」は組み込みと名前衝突しておかしくなってしまうためPjをSuffixした -->
  </div>
</template>

<script>
// -------------------------------------------------------------
// Pages
// -------------------------------------------------------------
import MainVisual from './pages/MainVisual.vue';
import Demonstration from './pages/Demonstration.vue';
import ReleaseNote from './pages/ReleaseNote.vue';
import FooterPj from './pages/FooterPj.vue';

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
    FooterPj,

    // -------------------------------------------------------------
    // Components
    // -------------------------------------------------------------
    ToggleVisbleAtScrollEvent,
    ScrollTopButton,
  },
};
</script>

<style lang="scss">
// -------------------------------------------------------------
// .scssファイルのインポート
// -------------------------------------------------------------
@import "styles/base/_normalize.scss";
@import "styles/base/_html_element.scss";
#app {
  overflow: hidden;
}
</style>
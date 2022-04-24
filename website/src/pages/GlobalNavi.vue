<template>
  <div id="navi-bar">
    <div id="pc-navi-bar">
      <HorizontalNaviBar>
        <NaviContents></NaviContents>
      </HorizontalNaviBar>
    </div>

    <div id="tab-navi-bar">
      <HamburgerMenu
        fadeinTime="0.5s" lineColor="#444" backgroundColor="#DDD">
        <NaviContents></NaviContents>
      </HamburgerMenu>
    </div>
  </div>
</template>

<script>
import NaviContents from '../pages/NaviContents.vue';
import HorizontalNaviBar from "../components/HorizontalNaviBar.vue";
import HamburgerMenu from "../components/HamburgerMenu.vue";
export default {
  components: {
    NaviContents,
    HorizontalNaviBar,
    HamburgerMenu,
  },
};
</script>

<style lang="scss">
@import "../styles/base/_variables.scss";

#navi-bar {
}

#pc-navi-bar{
  @include tab {
    display: none; // 水平ナビゲーションバーを非表示
  }
}

#tab-navi-bar{
  display: none; // ハンバーガーメニューを非表示

  @include tab {
    display: block; // ハンバーガーメニューを表示
  }
}
</style>
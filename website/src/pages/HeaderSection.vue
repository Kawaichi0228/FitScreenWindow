<template>
  <div id="header-section">
    <div class="header-inner">
      
      <h1 class="sam" @click="clickSmoothScroll('#app')">
        <span id="line01">Fit Screen Window</span>
      </h1>
      <GlobalNavi class="nav"></GlobalNavi>
    </div>
  </div>
</template>

<script>
import smoothScroll from '../methods/SmoothScroll.vue';
import GlobalNavi from "./GlobalNavi.vue";

export default {
  mixins: [smoothScroll],
  components: {
    GlobalNavi, // 上記mixinを使用する宣言
  },
};
</script>

<style lang="scss">
#header-section {
  /*画面上部に固定(「ウィンドウ全体」を基準に絶対値表示指定のため、背面要素の上から上書きされて描画される)*/
  position: fixed;
  top: 0;

  /* 画面上部に固定(ブロック要素として扱われるため、一番上の要素が隠れない) */
  /*position: sticky;*/
  /*top: 0; 追尾開始のスクロール位置(0で最上部から追尾開始)*/

  background-color: var(--theme-color-blackgray);
  width: 100%;
  z-index: 1;
}

.header-inner {
  margin-left: 5%;
  margin-right: 5%;
  display: flex;

  .sam {
    color: var(--theme-color-white);
    padding: 15px 0px;
    margin: unset;
    cursor: pointer;

    #line01 {
      margin: 0;
    }
  }

  .nav {
    margin: auto;
    margin-right: 0;
    padding: auto;
  }
}

</style>
<template>
  <div id="container">
    <transition name="foo">
      <div v-show="visible">
        <HeaderSectionSmall></HeaderSectionSmall>
      </div>
    </transition>
  </div>
</template>

<script>

import HeaderSectionSmall from '../pages/HeaderSectionSmall.vue';

export default {
  components: {
    HeaderSectionSmall,
  },

  data() {
    return {
      visible: true,
    };
  },

  created() {
    window.addEventListener("scroll", this.handleScroll);
  },

  props: {
    startPostionToVisible: Number,
    startPostionToHidden: Number
  },

  methods: {
    //MEMO: props と this. をなくしてコレのほうが簡単なのでは？(でも型定義できないか・・・)
    //handleScroll(startPostionToVisible, startPostionToHidden)
    handleScroll() {
      // 現在の画面スクロール位置を取得
      this.scrollY = window.scrollY;

      if (!this.visible) {
        // 定義した開始位置を、画面スクロール位置を超えたら表示する
        this.visible = window.scrollY > this.startPostionToVisible;

        // 定義した開始位置を、画面スクロール位置が下回ったら非表示にする
      } else if (window.scrollY < this.startPostionToHidden) {
        this.visible = !this.visible;
      }
    },
  },
};
</script>

<style lang="scss" scoped>

/* トランジションクラス */
/*<transition name="<name>">
</transition>*/

/* exp. */
/* .<name>-enter[-active, -to] */

/* (なにも付けない): transition 開始*/

#container {
  --foo-cssvar: 0.6s;

  .foo-enter {
    opacity: 0; /* 0:非表示 */
  }

  /* -active: transition している間 */
  .foo-enter-active,
  .foo-leave-active {
    transition: opacity var(--foo-cssvar); /* フェードの段階秒数(表示or非表示の切り替え間) */
  }

  /* -to: transition 終了*/
  .foo-enter-to {
    opacity: 1; /* 1:表示 */
  }
  .foo-leave-to {
    opacity: 0;
    transition: opacity var(--foo-cssvar); /* フェードの段階秒数(表示or非表示の切り替え間) */
  }
}

</style>
<template>
  <FadeInTransition fadeinTime="0.5s">
    <div v-show="visible">
      <slot name="fadein-slot"></slot>
    </div>
  </FadeInTransition>
</template>

<script>
import FadeInTransition from './FadeInTransition.vue';

export default {
  components: {
    FadeInTransition,
  },

  data() {
    return {
      visible: false,
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

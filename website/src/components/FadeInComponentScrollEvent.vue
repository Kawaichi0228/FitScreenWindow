<template>
  <div :class="{fadeIn: visible}">
    <slot v-show="visible"></slot>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        visible: false
      };
    },

    created() {
      window.addEventListener("scroll", this.handleScroll);
    },

    methods: {
      handleScroll() {
        // 画面最上部を取得
        var top = this.$el.getBoundingClientRect().top;

        if (!this.visible) {
          this.visible = top < window.innerHeight;

        // 定義した開始位置を、画面スクロール位置が下回ったら非表示にする
        } else if (window.scrollY < top) {
          this.visible = !this.visible;
        }

      }
    }
  }
</script>

<style>
.fadeIn {
  animation: fadeIn 1.5s;
}
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateX(-100px);
  }
  100% {
    opacity: 1;
    transform: translateX(0px);
  }
}
</style>
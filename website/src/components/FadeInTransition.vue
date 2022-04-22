<template>
  <div id="container" :style="[
      _fadeinTime
    ]"
  >
    <transition name="fade">
      <slot></slot>
    </transition>
  </div>
</template>

<script>
export default {
  props: {
    fadeinTime: {type: [Number, String], default: "1s"},
  },

  computed: {
    _fadeinTime() {return {'--fadeinTime': this.fadeinTime}}, //this = このコンポーネントのこと
  },
}
</script>

<style lang="scss" scoped>
/* トランジションクラス */
/*<transition name="<name>">
</transition>*/
/* exp. */
/* .<name>-enter[-active, -to] */

#container {
  /* (なにも付けない): transition 開始*/
  .fade-enter {
    opacity: 0; /* 0:非表示 */
  }

  /* -active: transition している間 */
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity var(--fadeinTime); /* フェードの段階秒数(表示or非表示の切り替え間) */
  }

  /* -to: transition 終了*/
  .fade-enter-to {
    opacity: 1; /* 1:表示 */
  }
  .fade-leave-to {
    opacity: 0;
    transition: opacity var(--fadeinTime);
  }
}
</style>
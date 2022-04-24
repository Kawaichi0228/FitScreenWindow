<template>
  <!-- ****************************** -->
  <!-- *** 引数をCSS変数へ渡す方法 *** -->
  <!-- ****************************** -->
  <!-- 「v-bind:style」でcomputedのプロパティをバインド -->
  <!-- - 配列[]を使うことで、複数のcomputedを指定できる -->
  <div
    class="fadein"
    :style="[
      _fadeinTime, 
      _beginPosY,
      _endPosY
    ]"
  >
    <slot></slot>
  </div>
</template>

<script>
export default {
  props: {
    fadeinTime: {type: [Number, String], default: "1s"},
    beginPosY: {type: [Number, String], default: "0px"},
    endPosY: {type: [Number, String], default: "0px"},
  },

  // CSS変数を定義して、CSS側に渡したいVueコンポーネントの値を指定する
  computed: {
    _fadeinTime() {return {'--fadeinTime': this.fadeinTime}}, //this = このコンポーネントのこと
    _beginPosY() {return {'--beginPosY': this.beginPosY}},
    _endPosY() {return {'--endPosY': this.endPosY}},
  },
}
</script>

<style lang="scss">
@import "../styles/base/_fadein.scss";

.fadein {
  //@prm
  //  fadein($fadeinTime, $beginPosY, $endPosY)
  /* computedで定義したCSS変数をvar()経由で使って、CSSの値を指定する */
  @include fadein(
                  var(--fadeinTime),
                  var(--beginPosY),
                  var(--endPosY),
                  );
}
</style>
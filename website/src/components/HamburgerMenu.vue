<template>
  <div id="hamburger-menu" :style="[
      _fadeinTime,
      _lineColor,
      _backgroundColor,
    ]"
  >
    <!--ハンバーガーメニューのボタン-->
    <div class="hamburger-button" @click='ActiveBtn=!ActiveBtn'>
      <span class="line line_01" :class="{'btn_line01':ActiveBtn}"></span>
      <span class="line line_02" :class="{'btn_line02':ActiveBtn}"></span>
      <span class="line line_03" :class="{'btn_line03':ActiveBtn}"></span>
    </div>
    <!--サイドメニュー-->
    <transition name="hamburger-menu">
      <div class="hamburger-menu" v-show="ActiveBtn">
        <slot></slot>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  props: {
    fadeinTime: {type: String},
    lineColor: {type: String},
    backgroundColor: {type: String},
  },

  computed: {
    _fadeinTime() {return {'--fadeinTime': this.fadeinTime}}, //this = このコンポーネントのこと
    _lineColor() {return {'--lineColor': this.lineColor}}, //this = このコンポーネントのこと
    _backgroundColor() {return {'--backgroundColor': this.backgroundColor}}, //this = このコンポーネントのこと
  },

  data() {
    return {ActiveBtn: false}
  },
};
</script>

<style lang="scss">
  #hamburger-menu {
    --p_fadeinTime: var(--fadeinTime);
    --p_lineColor: var(--lineColor);
    --p_backgroundColor: var(--backgroundColor);

    // ハンバーガーボタン全体
    .hamburger-button {
      // 画面基準にして、移動する距離を指定
      position: fixed;
      top: 10.5px;
      right: 50px;

      width: 70px;
      height: 72px;
      cursor: pointer;
      z-index: 50;

      // ハンバーガーの3本線
      .line {
      //3本線の色
      background: var(--p_lineColor);

      // 3本線の横幅と線の太さ
      width: 35px;
      height: 3px;

      position: absolute;
      top: 0;
      left: 20px;

      text-align: center;
      }
      .line_01 { // 1本目
      top: 16px;
      transition: var(--p_fadeinTime) ease;
      }
      .line_02 { // 2本目
      top: 26px;
      transition: var(--p_fadeinTime) ease;
      }
      .line_03 { // 3本目
      top: 36px;
      transition: var(--p_fadeinTime) ease;
      }
    }
    .btn_line01 {
      transform: translateY(10px) rotate(-45deg);
      transition: var(--p_fadeinTime) ease;
    }
    .btn_line02 {
      transition: var(--p_fadeinTime) ease;
      opacity: 0;
    }
    .btn_line03 {
      transform: translateY(-10px) rotate(45deg);
      transition: var(--p_fadeinTime) ease;
    }

    // ハンバーガーをクリックして開いたときのサイドメニュー
    .hamburger-menu-enter-active, .hamburger-menu-leave-active {
      transition: opacity var(--p_fadeinTime);
    }
    .hamburger-menu-enter, .hamburger-menu-leave-to {
      opacity: 0;
    }
    .hamburger-menu-leave, .hamburger-menu-enter-to{
      opacity: 1;
    }

    // NaviContentsの要素に対して操作
    .hamburger-menu {
      background-color: var(--p_backgroundColor);

      // 画面基準にして、移動する距離を指定
      position: fixed;
      top: 0;
      right: 0;

      z-index: 30;
      padding: 2rem 1rem;
      width: 300px;
      height: 80rem;

      ul{
      padding: 0;
      padding-top: 40px;
      }

      li {
      padding: 35px 0;
      list-style: none;
      line-height: 1;
      }

      a {
      color: rgb(66, 66, 66);
      text-decoration: none;
      font-size: 25px;
      margin: 0 4vw;
      padding-bottom: 8px;
      }
    }
  }
</style> 
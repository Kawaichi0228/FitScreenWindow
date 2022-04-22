<template>
  <div id="navicontents">
    <ul>
      <!-- TODO-001: ハンバーガーナビ内容がクリックされたら、HamburgerコンポーネントのActiveBtnに"False"の値を渡したい -->
      <li><a href="#" class="navi-button" @click="clickSmoothScroll('#Demonstration')">What is Fit Screen Window</a></li>
      <li><a href="#" class="navi-button" @click="clickSmoothScroll('#ReleaseNote')">更新履歴</a></li>
    </ul>
  </div>
</template>

<script>
import smoothScroll from '../methods/SmoothScroll.vue';

export default {
  mixins: [smoothScroll], // 読み込んだmethodsの使用宣言
};
</script>

<style>
#navicontents {
}

.navi-button {
  position: relative;
  display: inline-block;
  font-weight: bold;
  padding: 0.25em 10px;
  text-decoration: none;
  margin-right:10px;
  margin-left: 10px;
  outline: none;
}
.navi-button:before {
  position: absolute;
  content: '';
  width: 100%;
  height: 1px;
  top:100%;
  left: 0;
  border-radius: 0.5px;
  background:var(--theme-color-gray); /* 文字下線の色 */
  transition: .3s;
}
.navi-button:hover:before {
  top: -webkit-calc(100% - 3px);
  top: calc(100% - 3px);
}
</style>




<template>
    <div id="scroll-top-button">
        <!-- MEMO: 「href=""」を記述しないとマウスオンしてもカーソル変わらないため必要 -->
      <a href="" @click="clickSmoothScroll('#app')"></a>
    </div>
</template>

<script>
import smoothScroll from '../methods/SmoothScroll.vue';
export default {
  mixins: [smoothScroll] // 上記mixinを使用する宣言
};
</script>

<style>
/* -------------------------------------------------------- */
/* スクロールトップボタン */
/* -------------------------------------------------------- */
#scroll-top-button {
  /* ボタンの大きさ */
  --page-top-width-and-height: 70px;
  width: var(--page-top-width-and-height);
  height: var(--page-top-width-and-height);

  /* ボタンの表示位置 */
  position: fixed; /* 「ウィンドウ全体」を基準に絶対値表示指定 */
  right: 20px;
  bottom: 20px;

  background: var(--theme-color-gray);
  border-radius: 50%;
  opacity: 0.6;
  z-index: 1; /* レイヤー前面背面順 */
}

#scroll-top-button a{
  /* ボタンの大きさ */
  width: var(--page-top-width-and-height);
  height: var(--page-top-width-and-height);

  position: relative;
  display: block;
  text-decoration: none;
}
#scroll-top-button a::before{
  /* 上矢印の大きさ */
  --page-top-uparrow: 50px;
  font-size: var(--page-top-uparrow);
  width: var(--page-top-uparrow);
  height: var(--page-top-uparrow);

  font-family: 'Font Awesome 5 Free';
  font-weight: 900;
  content: '\f106';
  color: var(--theme-color-white);
  position: absolute;
  top: -8px;
  bottom: 0;
  right: 0;
  left: 0;
  margin: auto;
  text-align: center;
}
</style>
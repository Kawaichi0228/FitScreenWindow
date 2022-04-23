<template>
  <div id="Demonstration">
    <h1 id="content-title">アクティブウィンドウを すばやく画面にフィット</h1>
    <img id="main-image" src="../assets/demonstration.gif" alt="" />
    <p>それぞれフィットさせたいウィンドウをアクティブにした状態で<br>
    ショートカットキーを押すごとに最大4段階のサイズ変化 + 画面の端に<br>
    合わせるように自動的に配置します。</p>
    <p>[ショートカットキー]</p>
    <p>ウィンドウ左寄せ：Ctrl + Alt + ←</p>
    <p>ウィンドウ右寄せ：Ctrl + Alt + →</p>
  </div>
</template>

<style scoped>
#Demonstration{
  padding: var(--section-padding);
  background-color: var(--theme-color-white);
}

#main-image{
  height: 250px;
}
</style>

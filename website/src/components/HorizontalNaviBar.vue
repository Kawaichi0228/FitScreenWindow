<template>
  <div id="horizontal-navi-bar">
    <slot></slot>
  </div>
</template>

<style lang="scss">
// NaviContentsの要素に対して操作
#horizontal-navi-bar {
  ul {
    display: flex; // li要素を横並びにする
  }

  li {
    list-style: none; // 初期の点(・)を非表示にする
  }
}
</style>
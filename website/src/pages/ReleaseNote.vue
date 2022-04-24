<template>
  <div id="ReleaseNote">

    <div id="SeparatorLine">
      <h1>バージョン履歴</h1>
      <hr>
    </div>

    <div id="release-list">
      <ul>
        <li><b>[更新日:2022/4/21 バージョン:1.0(for <b>Python</b>)]</b>
          <br>リニューアル公開しました。</li>
        <li><b>[更新日:2022/3/08 バージョン:1.0.0.0(for Autohotkey)]</b>
          <br>初回版を公開しました。</li>
      </ul>
    </div>
    
  </div>
</template>

<script>
</script>

<style lang="scss" scoped>
div#ReleaseNote{
  padding: var(--section-padding);
  background-color: var(--theme-color-whitelightgray);

div#release-list{
  display: flex;
  justify-content: center;
  
  ul {
    list-style: disc;
    line-height: 25pt;
  }
  li {
    text-align:left;
    margin:30px 0px;
  }
}
}
</style>
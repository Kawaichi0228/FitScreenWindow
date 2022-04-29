<template>
  <div id="ReleaseNote">

    <div id="SeparatorLine">
      <h1>バージョン履歴</h1>
      <hr>
    </div>

    <div id="release-list">
      <ul>
        <li><b>[更新日:2022/4/29 バージョン:1.0(for Python)]</b>
          <br>リニューアル版を公開しました。</li>
        <li><b>[更新日:2022/3/08 バージョン:1.0.0.0(for Autohotkey)]</b>
          <br>初回版を公開しました。</li>
      </ul>
    </div>
    
  </div>
</template>

<script>
</script>

<style lang="scss" scoped>
@import "../styles/base/_variables.scss";
@import "../styles/base/_mixin.scss";

h1 {
  font-size: $font-size-h2;
}

// TODO: hrタグを共通化
hr {
	border-top: 3px solid $color-lightgray;
  width: 80%;
}

div#ReleaseNote{
  padding: $section-padding;
  background-color: $color-whitelightgray;

div#release-list{
  @include horizontal-center;
  
  ul {
    list-style: disc;
    line-height: 25pt;
  }
  li {
    text-align: left;
    margin: 30px 0px;
  }
}
}
</style>
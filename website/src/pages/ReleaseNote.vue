<template>
  <div id="ReleaseNote">

    <div id="SeparatorLine">
      <h1>バージョン履歴</h1>
      <hr>
    </div>

    <div id="release-list">
      <ul>
        <li><b>[更新日:2022/6/9 バージョン:4.1]</b>
          <br>仕様変更しました。</li>
        <li><b>[更新日:2022/6/4 バージョン:4.0]</b>
          <br>機能追加および仕様変更しました。</li>
        <li><b>[更新日:2022/5/16 バージョン:3.0]</b>
          <br>機能追加および仕様変更しました。</li>
        <li><b>[更新日:2022/5/11 バージョン:2.2]</b>
          <br>不具合を修正および仕様変更しました。</li>
        <li><b>[更新日:2022/5/8 バージョン:2.1]</b>
          <br>機能を追加しました。</li>
      </ul>
    </div>
    <span>and more...</span><br>
    <span class="releases-description">(上記以前の変更及び変更点の詳細等は
      <a href="https://github.com/Kawaichi0228/FitScreenWindow/releases">
        GitHub
      </a>
    より確認できます)</span>

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

.releases-description {
  font-size: $font-size-small;

  a {
    text-decoration: underline;
    &:hover {text-decoration: none;}
  }
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
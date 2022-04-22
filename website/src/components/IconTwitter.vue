<template>
  <div :stlye="[_cssUnHover, _cssHover,]">
    <a
      :href="url"
      class="link-icon"
      target="_blank"
      rel="noreferrer"
      >
      <font-awesome-icon
        :icon="['fab', 'twitter']"
        class="web-icon twitter"
      />
    </a>
  </div>
</template>

<script>
export default {
  // 外部から引数を渡すための引数名を宣言
  props: {
    url: {type: String},
    cssUnHover: {type: String},
    cssHover: {type: String},
  },

  // CSS変数を定義して、CSS側に渡したいVueコンポーネントの値を指定する
  computed: {
    _cssUnHover() {return {'--cssUnHover': this.cssUnHover}}, //this = このコンポーネントのこと
    _cssHover() {return {'--cssHover': this.cssHover}},
  }
}
</script>

<style lang="scss" scoped>
@import "../styles/_mixin.scss";

.link-icon {
  margin: 0px 16px 0px 0px; /* アイコン同士のマージン */
  @include tab {
    margin: 0px 8px 0px 8px; /* アイコン同士のマージン */
  }
}

.web-icon {
  font-size: 2em; /* アイコンの大きさ */
  background-color: var(--cssUnHover);
  padding: 0.3em;
  border-radius: 50%;
}
.web-icon:hover {
  color: var(--cssUnHover);
}

.twitter {
  color: var(--cssHover);
}
.twitter:hover {
  background-color: var(--cssHover);
}
</style>
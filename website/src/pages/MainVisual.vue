<template>
  <div id="main-visual">
    <FadeInComponent fadeinTime="1s" beginPosY="-100px" endPosY="0px">
      
      <div id="title-wrap">
        <div id="logo-short-wrap">
          <img id="logo-short" src="../assets/logo-short.png" alt="" />
        </div>
        <h1 id="main-text">Fit Screen Window</h1>
      </div>
      <h2 id="main-text2">for Windows</h2>
    
        <div id="button-wrap">
          <a href="https://github.com/Kawaichi0228/FitScreenWindow/releases/download/v4.1/FitScreenWindow-v4.1-Installer.zip">
            <button class="btn">Download v4.1</button>
          </a>
        </div>
      
      <div id="github-wrap">
        <div id="github-hoverarea">
          <a href="https://github.com/Kawaichi0228/FitScreenWindow" target="_blank" rel="noreferrer"> <!-- _blankを指定したら必ずnoreferrerを入れる-->
            <span class="github-text">GitHub Project Page</span>
          </a>
          <a href="https://github.com/Kawaichi0228/FitScreenWindow" target="_blank" rel="noreferrer">
            <font-awesome-icon :icon="['fab', 'github']" class="github"/>
          </a>
        </div>
      </div>
    </FadeInComponent>

    <img id="main-image" src="../assets/mainvisual.png" alt="" />

  </div>
</template>

<script>
import FadeInComponent from "../components/FadeInComponent.vue";

export default {
  components: {
    FadeInComponent,
  },
};
</script>


<style lang="scss" scoped>
@import "../styles/base/_mixin.scss";
@import "../styles/base/_variables.scss";
@import "../styles/function/_rem.scss";

div#main-visual {
  overflow: hidden; // ブロックからはみ出した要素を隠す
  padding-top: rem(40);
  background-color: $color-lightred;
  color: $color-white;
}

div#title-wrap {
  @include center;

  @include tab {
    display: block;
  }

  h1#main-text {
    font-size: $font-size-title-firstrow;
    font-weight: bold;
    margin: 0px;
  }

  div#logo-short-wrap {
    img#logo-short {
      height: rem(80);
      margin-right: rem(30);
    }
  }
}

h2#main-text2 {
  font-size: $font-size-title-secondrow;
  font-weight: bold;
  margin: 0;
}

img#main-image {
  width: 100%;
  max-width: rem(450);
  position: relative;
  bottom: rem(-10);
}

div#button-wrap {
  margin: rem(30);
  
  button.btn {
      font-size: $font-size-h2;
      font-weight: bold;
      background-color: $color-white;
      color: $color-gray;

      padding: rem(16) rem(50); // ボタンの大きさ
      border-radius: 6px; // 線の丸み
      border: 3px solid $color-gray;
      box-shadow: 0 1px 4px rgba(0, 0, 0, .2);
      transition: .3s;

      display: inline-block;
      position: relative;
      text-align: center;
      text-decoration: none;
      
      &:hover {
          cursor: pointer; // マウスオン時にカーソルを指にする(aタグのように)
          background-color: $color-lightblue;
          color: $color-white;
          letter-spacing: 0.2rem;
      }
  }
}

div#github-wrap {
  @include horizontal-center;
  
  div#github-hoverarea {
    @include center;

    height: rem(30);
    margin-bottom: rem(14);
    font-size: $font-size-h2;
    
    transition: 0.3s;
    &:hover {
      text-shadow: 0px 12px 24px rgba(20, 146, 175, 0.4);
      transform: translateY(-10px);
    }

    a {
      color: $color-white;
    }

    .github-text {
      font-size: $font-size-base;
      text-decoration: underline;
    }

    .github {
      color: $color-white;
      margin-left: rem(15);
      font-size: 2em; /* アイコンの大きさ */
    }
  }
}
</style>
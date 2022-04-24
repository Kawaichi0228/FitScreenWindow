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
          <a href="https://github.com/Kawaichi0228/FitScreenWindow/releases/download/v1.0/FitScreenWindow-1.0.zip">
            <button class="btn">Download v1.0</button>
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

div#main-visual {
  overflow: hidden; // ブロックからはみ出した要素を隠す
  padding-top: 60px;
  background-color: var(--theme-color-lightred);
  color: var(--theme-color-white);
}

div#title-wrap {
  // ---垂直中央寄せ---
  display: flex;
  flex-direction: row;
  justify-content: center; // 水平中央
  align-items: center; // 垂直中央

  @include tab {
    display: block;
  }

  h1#main-text {
    font-weight: bold;
    margin: 0px;

    font-size: 54pt;
    @include tab {
      font-size: 34pt;
    }
  }

  div#logo-short-wrap {
    img#logo-short {
      height: 80px;
      margin-right: 30px;
    }
  }
}

h2#main-text2 {
  font-size: 20pt;
  font-weight: bold;
  margin: 0px;
}

img#main-image {
  width: 100%;
  max-width: 400px;

  margin-top: 15px;
  position: relative;
  bottom: -10px;

  @include tab {
    height: 300px;
  }
}

div#button-wrap {
  margin: 30px;
  
  button.btn {
      font-size: 18pt;
      font-weight: bold;
      background-color: var(--theme-color-white);
      color: var(--theme-color-gray);

      border-radius: 6px; // 線の丸み
      border: 3px solid var(--theme-color-gray);
      box-shadow: 0 1px 4px rgba(0, 0, 0, .2);
      padding: 18px 60px;
      transition: .3s;

      display: inline-block;
      position: relative;
      text-align: center;
      text-decoration: none;
      
      &:hover {
          cursor: pointer; // マウスオン時にカーソルを指にする(aタグのように)
          background-color: var(--theme-color-lightblue);
          color: var(--theme-color-white);
          letter-spacing: 0.2rem;
      }
  }
}

div#github-wrap {
  // ---垂直中央寄せ---
  display: flex;
  flex-direction: row;
  justify-content: center; // 水平中央
  // -----------------------------
  
  div#github-hoverarea {
    width: 300px;
    height: 60px;
    font-size: 20px;

    display: flex;
    flex-direction: row;
    justify-content: center; // 水平中央
    align-items: center; // 垂直中央
    
    transition: 0.3s;
    &:hover {
      text-shadow: 0px 12px 24px rgba(20, 146, 175, 0.4);
      transform: translateY(-10px);
    }

    a {
      color: var(--theme-color-white);
    }

    .github-text {
      text-decoration: underline;
    }

    .github {
      color: var(--theme-color-white);
      margin-left: 15px;
      font-size: 2.3em; /* アイコンの大きさ */
    }
  }
}
</style>
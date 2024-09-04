import { extendTheme } from "@chakra-ui/react";

const theme = extendTheme({
  colors: {
    background: "#070720",
    text: "white",
    border: "#149C3A",
    secondary: "#191937",
    terciary: "#3273FA",
    win: "#1E2B5E",
    lose: "#3E223B",
    ligthBlueText: "#C1D0F2",
    orangeText: "#FF9B00",
    redText: "#FF4E50",
  },

  fonts: {
    heading: "Inter, sans-serif",
    body: "Inter, sans-serif",
  },

  styles: {
    global: {
      body: {
        backgroundColor: "background",
        margin: 0,
        fontFamily: "Inter, sans-serif",
        color: "text",
      },
      html: {
        height: "100%",
      },
      "#root": {
        height: "100%",
      },
    },
  },
});

export default theme;

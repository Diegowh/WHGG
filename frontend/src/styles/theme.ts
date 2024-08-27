import { extendTheme } from "@chakra-ui/react";

const theme = extendTheme({
  colors: {
    background: "#202124",
    text: "white",
    border: "#149C3A",
    secondary: "#31313C",
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

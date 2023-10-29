// styles.js
import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    // justifyContent: "center",
    padding: 20,
    backgroundColor: "#211A1D",
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 20,
  },
  input: {
    color: "white",
    height: 40,
    borderColor: "gray",
    borderWidth: 1,
    marginBottom: 10,
    padding: 10,
    width: "100%",
    marginTop: 20,
    borderRadius: 10,
  },
  answer: {
    color: "#DDDBCB",
    marginTop: 20,
    fontSize: 18,
  },
  button: {
    // height: 40,
    // borderColor: "gray",
    // borderWidth: 1,
    marginBottom: 10,
    padding: 10,
    width: "25%",
    marginTop: 20,
    borderRadius: 10,
    backgroundColor: "#FFDD58",
  },
});

export default styles;

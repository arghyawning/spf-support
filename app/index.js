import React, { useState } from "react";
import { View, Text, TextInput, Button, TouchableOpacity } from "react-native";
import styles from "./styles";
import { Stack } from "expo-router";

const Home = () => {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleQuestionSubmit = async () => {
    try {
      console.log({ question: question });
      const response = await fetch("http://192.168.23.216:5000/get_answer", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question: question }),
      });
      console.log(response);

      const data = await response.json();
      setAnswer(data.answer);
    } catch (error) {
      console.error("Error fetching answer:", error);
    }
  };

  return (
    <View style={styles.container}>
      <Stack.Screen
        options={{
          headerTitle: "Mediklik",
          headerStyle: {
            backgroundColor: "#008080",
          },
          headerTitleStyle: {
            color: "#DDDBCB",
            // textAlign: "center",
            // fontSize: 25,
            fontWeight: "bold",
            // backgroundColor: "#008080",
          },
        }}
      />
      {/* <Text style={styles.title}>Home</Text> */}

      <TextInput
        style={styles.input}
        placeholder="Ask me anything..."
        placeholderTextColor="#807c7c"
        value={question}
        onChangeText={(text) => setQuestion(text)}
      />

      {/* <Button
        title="Search"
        onPress={handleQuestionSubmit}
        style={styles.button}
      /> */}

      <TouchableOpacity style={styles.button} onPress={handleQuestionSubmit}>
        <Text style={{ color: "black", textAlign: "center", fontSize: 17 }}>
          Search
        </Text>
      </TouchableOpacity>

      {answer !== "" && <Text style={styles.answer}>{answer}</Text>}
    </View>
  );
};

export default Home;

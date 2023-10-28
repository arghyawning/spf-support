import React, { useState } from "react";
import { View, Text, TextInput, Button } from "react-native";
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
        // body: JSON.stringify({ "question" : question }),
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
      <Stack.Screen options={{ headerTitle: "spf-support" }} />
      <Text style={styles.title}>Home</Text>

      <TextInput
        style={styles.input}
        placeholder="Ask me anything..."
        value={question}
        onChangeText={(text) => setQuestion(text)}
      />

      <Button title="Get Answer" onPress={handleQuestionSubmit} />

      {answer !== "" && <Text style={styles.answer}>{answer}</Text>}
    </View>
  );
};

export default Home;

import { StyleSheet, Text, View, SafeAreaView, StatusBar, TextInput, Button } from "react-native";
import React from "react";
import { Formik } from "formik";
import * as yup from "yup";
// eslint-disable-next-line import/no-extraneous-dependencies
import { NavigationContainer } from "@react-navigation/native";
// eslint-disable-next-line import/no-extraneous-dependencies
import { createStackNavigator } from "@react-navigation/stack";

const loginValidationSchema = yup.object().shape({
    email: yup.string().email("Please enter valid email").required("Email Address is Required"),
});

const styles = StyleSheet.create({
    loginContainer: {
        width: "80%",
        alignItems: "center",
        padding: 10,
        elevation: 10,
        backgroundColor: "#e6e6e6",
    },
    textInput: {
        height: 40,
        width: "100%",
        margin: 10,
        backgroundColor: "white",
        borderColor: "gray",
        borderWidth: StyleSheet.hairlineWidth,
        borderRadius: 10,
    },
});

// @ts-ignore
function HomeScreen({ navigation }) {
    return (
        <View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
            <Button title="Go to Login Screen" onPress={() => navigation.navigate("Login")} />
        </View>
    );
}

function Login() {
    return (
        <>
            <StatusBar barStyle="dark-content" />
            <SafeAreaView style={styles.loginContainer}>
                <View>
                    <Text>Login Screen</Text>
                </View>
            </SafeAreaView>
            <Formik validationSchema={loginValidationSchema} initialValues={{ email: "" }} onSubmit={() => {}}>
                {({ handleChange, handleBlur, handleSubmit, values, errors, isValid }) => (
                    <>
                        <TextInput
                            placeholder="Email Address"
                            style={styles.textInput}
                            onChangeText={handleChange("email")}
                            onBlur={handleBlur("email")}
                            value={values.email}
                            keyboardType="email-address"
                        />
                        {errors.email && <Text style={{ fontSize: 10, color: "red" }}>{errors.email}</Text>}
                        <Button onPress={handleSubmit} title="LOGIN" disabled={!isValid} />
                    </>
                )}
            </Formik>
        </>
    );
}

const Stack = createStackNavigator();

function MyStack() {
    return (
        <Stack.Navigator>
            <Stack.Screen name="Home" component={HomeScreen} />
            <Stack.Screen name="Login" component={Login} />
        </Stack.Navigator>
    );
}

export default function App() {
    return (
        <NavigationContainer>
            <MyStack />
        </NavigationContainer>
    );
}

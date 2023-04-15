import { View, Button } from "react-native";
import React from "react";
// eslint-disable-next-line import/no-extraneous-dependencies
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
// @ts-ignore
import Login from "components/Login";

// @ts-ignore
function HomeScreen({ navigation }: { navigation: type }) {
    return (
        <View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
            <Button title="Go to Login Screen" onPress={() => navigation.navigate("Login")} data-testid="login__btn" />
        </View>
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

import { useEffect, useState } from "react";

function getValueFromLocalStorage<T>(key: string, defaultValue: T) {
    const storage = localStorage.getItem(key);
    if (storage) return JSON.parse(storage).value as T;
    return defaultValue;
}

function setStateToLocalStorage<T>(key: string, value: T) {
    localStorage.setItem(key, JSON.stringify({ value }));
}

function useLocalStorage<T>(key: string, defaultValue: T): [T, (value: T | ((prev: T) => T)) => void] {
    const initialValue = getValueFromLocalStorage(key, defaultValue);
    const [value, setValue] = useState<T>(initialValue);

    useEffect(() => {
        setStateToLocalStorage(key, value);
    }, [value, defaultValue]);

    return [value, setValue];
}

export default useLocalStorage;

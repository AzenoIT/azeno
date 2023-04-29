import resolveConfig from "tailwindcss/resolveConfig";
import config from "../tailwind.config.js";

// Unfortunately tailwind is not typed and typing libs support only native schema
export default resolveConfig(config) as any; // eslint-disable-line @typescript-eslint/no-explicit-any

import React from "react";
import { render, fireEvent, screen } from "@testing-library/react";
import { deeplyRenderComponentWithRedux } from "../test-utils";
import Leaderboard from "./Leaderboard";

test("Should render leaderboard page", () => {
  const { getByText } = deeplyRenderComponentWithRedux(<Leaderboard />);
  expect(getByText("Game Leaderboard")).toBeInTheDocument();
});
